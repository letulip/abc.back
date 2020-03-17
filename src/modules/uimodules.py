from tornado.web import UIModule


class PageHeader(UIModule):
	def render(self):
		return self.render_string(
			"modules/module_page_header.html"
		)


class NavTree(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_nav_tree.html",
			module_data = data
		)


class NavTop(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_nav_top.html",
			module_data = data
		)


class ShponTable(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_shpon_table.html",
			module_data = data
		)


class PageFooter(UIModule):
	def render(self):
		return self.render_string(
			"modules/module_page_footer.html"
		)