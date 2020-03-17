from tornado.web import UIModule


class ShponTable(UIModule):
	def render(self, data):
		return self.render_string(
			"module_shpon_table.html",
			module_data = data
		)