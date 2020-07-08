from tornado.web import UIModule


class PageHeader(UIModule):
	def render(self):
		return self.render_string(
			"modules/module_page_header.html"
		)


class NavTree(UIModule):
	def render(self, data, *args):
		return self.render_string(
			"modules/module_nav_tree.html",
			module_data = data,
			active_nav_item = args[0],
			active_nav_item_second = args[1],
			active_nav_item_third = args[2]
		)


class NavTop(UIModule):
	def render(self, data, uri, *args):
		# print(args[1])
		return self.render_string(
				"modules/module_nav_top.html",
				module_data = data,
				module_uri = uri,
				module_material = args[0],
				active_nav_item = args[1]
			)
		

class ShponTabs(UIModule):
	def render(self, data, material, category):
		return self.render_string(
			"modules/module_shpon_tabs.html",
			module_data = data,
			module_material = material,
			module_uri = category
		)


class ShponTable(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_shpon_table.html",
			module_data = data
		)


class ShponViews(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_shpon_views.html",
			module_data = data
		)


class JointsTabs(UIModule):
	def render(self, data, material, category):
		return self.render_string(
			"modules/module_joints_tabs.html",
			module_data = data,
			module_material = material,
			module_uri = category
		)


class JointsTable(UIModule):
	def render(self, data):
		return self.render_string(
			"modules/module_joints_table.html",
			module_data = data
		)


class PageFooter(UIModule):
	def render(self):
		return self.render_string(
			"modules/module_page_footer.html"
		)