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
		(row, col) = self.view.rowcol(self.view.sel()[0].begin())
		pt = self.view.text_point(row + nlines, col)
		self.view.sel().clear()
		self.view.sel().add(sublime.Region(pt))
		self.view.show(pt)

class multi_up_select(sublime_plugin.TextCommand):
	def run(self, edit, nlines):
		for i in range(nlines):
			self.view.run_command('move', {"by": "lines", "forward": False, "extend":True})
		
class multi_down_select(sublime_plugin.TextCommand):
	def run(self, edit, nlines):
		for i in range(nlines):
			self.view.run_command('move', {"by": "lines", "forward": True, "extend":True})