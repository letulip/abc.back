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
				self.render('error.heml', status_code = status_code, reason = self._reason)
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
			test_data = test_data
		)


class TestPage(BaseHandler):

	def renderTable(self, data):
		# data = self.get_argument()
		table = self.render_string(
			'templates/dv_table.html',
			test_data = data
		)

		return table

	def get(self):
		mat_type = (self.request.uri).split('/')[2]
		self.render(
			'{0}_test.html'.format(mat_type),
			test_data = test_data[mat_type],
			table_data = self.renderTable(test_data[mat_type])
		)


# def renderTableFatory(self, data):
# 	def renderTable():
# 		return (self.render_string('dv_table.html', test_data=data))
# 	return renderTable

# class SubTest(BaseHandler):
# 	def get(self):
# 		self.render('sub.html', 
# 			test_data = test_data['dv'],
# 			renderTable = renderTableFatory(self, test_data['dv'])
# 		)


class SubTest(BaseHandler):

	def renderTable(self, data):
		# data = self.get_argument()
		table = self.render_string(
			'templates/dv_table.html',
			test_data = data
		)

		return table

	def get(self, uri):
		# self.redirect(uri)
		self.render(
			'templates/{0}_test.html'.format(uri),
			test_data = test_data[uri],
			table_data = self.renderTable(test_data[uri]['material']),
			module_data = test_data[uri]
		)


class App(Application):

	def __init__(self):

		handlers = [
			('/', HomePage),
			('/catalog', CatalogPage),
			# ('/catalog/dv', TestPage),
			# ('/catalog/dvg', TestPage),
			(r'/catalog/(.+)', SubTest),
			# ('/sb_test', SubTest)
		]

		settings = dict(
			debug = True,
			autoreload = True,
			ui_modules = uimodules
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