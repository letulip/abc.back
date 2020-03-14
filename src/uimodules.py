from tornado.web import UIModule


class dvTable(UIModule):
	def render(self, data):
		return self.render_string(
			"module_table.html",
			module_data = data
		)