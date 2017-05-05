import sublime
import sublime_plugin

class multi_up(sublime_plugin.TextCommand):
	def run(self, edit, nlines):
		(row, col) = self.view.rowcol(self.view.sel()[0].begin())
		pt = self.view.text_point(row - nlines, 0)
		self.view.sel().clear()
		self.view.sel().add(sublime.Region(pt))
		self.view.show(pt)

class multi_down(sublime_plugin.TextCommand):
	def run(self, edit, nlines):
		screenful = self.view.visible_region()
		(row, col) = self.view.rowcol(self.view.sel()[0].begin())
		pt = self.view.text_point(row + nlines, col)
		self.view.sel().clear()
		self.view.sel().add(sublime.Region(pt))
		self.view.show(pt)