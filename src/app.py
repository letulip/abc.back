import sys
import os
import traceback
import json

from logging import (debug, info, warning, error, exception)

from tornado.web import (Application, RedirectHandler, RequestHandler,
                         StaticFileHandler, HTTPError)
from tornado.ioloop import IOLoop
from tornado.options import (parse_config_file, parse_command_line, define, options)
from tornado import (autoreload, gen)
from tornado.httpclient import AsyncHTTPClient

from data import data as test_data


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

        self.render('index.html')


class TestPage(BaseHandler):

    def get(self):

        self.render(
            'test.html',
            test_data = test_data
            )


class App(Application):

    def __init__(self):

        handlers = [
            ('/', HomePage),
            ('/test', TestPage),
        ]

        settings = dict(
            debug = True,
            autoreload = True
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