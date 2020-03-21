import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # python-3.8.0a4

import sys
import os
import traceback
import json
import html

from logging import (debug, info, warning, error, exception)

from tornado.web import (Application, RedirectHandler, RequestHandler,
						 StaticFileHandler, HTTPError, UIModule)
from tornado.ioloop import IOLoop
from tornado.options import (parse_config_file, parse_command_line, define, options)
from tornado import (autoreload, gen)
from tornado.httpclient import AsyncHTTPClient

# local imports
from data import data as test_data
from modules import uimodules

define('port', default = 9008, help = 'port to run on', type = int)
define('site_url', default = 'localhost', help = 'site URL')

webapp_path = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.realpath(os.path.join(webapp_path, './static'))
template_path = os.path.realpath(os.path.join(webapp_path, 'templates'))
module_path = os.path.realpath(os.path.join(webapp_path, 'modules'))


class MixinCustomHandler():

	def write_error(self, status_code, **kwargs):
		info('%d <- :: write_error' % status_code)
		try:
			if self.settings.get('serve_traceback') and 'exc_info' in kwargs:
				self.set_header('Content-Type', 'text/plain')
				for line in traceback.format_exception(*kwargs['exec_info']):
					self.write(line)
				self.finish()
			else:
				self.render('error.html', status_code = status_code, reason = self._reason)
		except Exception as err:
			exception(err)
			self.set_header('Content-Type', 'text/plain')
			self.write('500: EPIC SERVER FAIL. PLEASE, TRY AGAIN LATER')
			self.finish()

	def render(self, template_name, **kwargs):
		RequestHandler.render(self,
			template_name,
			site_url = options.site_url,
			**kwargs)


class BaseHandler(MixinCustomHandler, RequestHandler):
	
	def render(self, template_name, **kwargs):
		RequestHandler.render(self,
			template_name,
			site_url = options.site_url,
			**kwargs)


class CustomStatic(MixinCustomHandler, StaticFileHandler):
    render = MixinCustomHandler.render


class TestPageBaseHandler(BaseHandler):

	def render(self, template_name, **kwargs):
		# TODO
		pass


class HomePage(BaseHandler):

	def get(self):

		self.render(
			'index.html',
			test_data = test_data
		)


class CatalogPage(BaseHandler):
	def get(self):
		self.render(
			'catalog.html',
			test_data = test_data,
			module_uri = 0,
			active_nav_item = False,
			active_nav_item_second = False,
			active_nav_item_third = False
		)


class ModuleShponMain(BaseHandler):

	def get(self):
		self.render(
			'shpon.html',
			test_data = test_data['shpon'],
			module_uri = 0,
			common_data = test_data,
			active_nav_item = 'shpon',
			active_nav_item_second = False,
			active_nav_item_third = False
		)


def ParseUri(uri):
	return uri.split('/')


class ModuleShponDetail(BaseHandler):

	def get(self, uri):
		path = ParseUri(uri)
		make_path = path[0]
		material_path = 0
		if len(path) > 1:
			material_path = path[1]
		# print(material_path)
		self.render(
			'shpon_content_layout.html',
			# test_data = test_data[uri],
			# table_data = self.renderTable(test_data[uri]['material']),
			module_uri = make_path,
			module_uri_material = material_path,
			module_data = test_data['shpon']['dir_contents'][make_path],
			common_data = test_data,
			active_nav_item = 'shpon',
			active_nav_item_second = make_path,
			active_nav_item_third = material_path
		)


class ModuleJointsMain(BaseHandler):

	def get(self):
		self.render(
			'joints.html',
			test_data = test_data['joints'],
			module_uri = 0,
			common_data = test_data,
			active_nav_item = 'joints',
			active_nav_item_second = False,
			active_nav_item_third = False
		)


class ModuleJointsDetail(BaseHandler):

	def get(self, uri):
		path = ParseUri(uri)
		make_path = path[0]
		material_path = 0
		if len(path) > 1:
			material_path = path[1]
		# print(material_path)
		self.render(
			'joints_content_layout.html',
			# test_data = test_data[uri],
			# table_data = self.renderTable(test_data[uri]['material']),
			module_uri = make_path,
			module_uri_material = material_path,
			module_data = test_data['joints']['dir_contents'][make_path],
			common_data = test_data,
			active_nav_item = 'joints',
			active_nav_item_second = make_path,
			active_nav_item_third = material_path
		)


class App(Application):

	def __init__(self):

		handlers = [
			('/', HomePage),
			('/catalog', CatalogPage),
			('/catalog/shpon', ModuleShponMain),
			(r'/catalog/shpon/(.+)', ModuleShponDetail),
			('/catalog/joints', ModuleJointsMain),
			(r'/catalog/joints/(.+)', ModuleJointsDetail),
			(r'/(.*)', CustomStatic, {'path': static_path})
		]

		settings = dict(
			debug = True,
			autoreload = True,
			ui_modules = uimodules,
			static_path = static_path,
			template_path = template_path,
			# module_path = module_path,
		)
	
		Application.__init__(self, handlers, **settings)


def main():
	if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
		parse_config_file(sys.argv[1])
		parse_command_line(sys.argv[1:])
	else:
		warning('Running without config: terminate')
		print('Example usage:')
		print(' python main.py /path/to/production.conf [params]')
		exit()

	app = App()
	app.listen(options.port)

	info('Port %s' % options.port)

	autoreload.start()
	IOLoop.instance().start()


if __name__ == '__main__':
	main()