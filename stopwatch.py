#!/usr/bin/env python

import datetime

import pygtk
pygtk.require("2.0")
import gtk
import gobject


ONE_SECOND = datetime.timedelta(seconds=1)


class Stopwatch(object):
	def __init__(self):
		# The actual stopwatch/time content
		self.elapsed_time = datetime.timedelta()
		self.enabled = False

		# Create the actual stopwatch window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_resizable(False)
		self.window.set_default_size(-1, 50)
		self.window.set_border_width(10)
		self.window.set_title("stopwatch")
		self.window.show()

		# Install callbacks
		self.window.connect("destroy", self.destroy)
		gobject.timeout_add(1000, self.refresh_time)

		# Window layout
		box = gtk.VBox(True, 0)

		self.time = gtk.Label(str(self.elapsed_time))
		self.time.set_width_chars(8)	# "hh:mm:ss"
		box.pack_start(self.time, True, True, 0)
		self.time.show()

		self.button = gtk.Button("Start")
		self.button.connect("clicked", self.toggle_time)

		box.pack_start(self.button, True, True, 0)
		self.button.show()

		self.window.add(box)
		box.show()

		return


	def destroy(self, widget, data=None):
		gtk.main_quit()


	def refresh_time(self):
		if (self.enabled):
			self.elapsed_time += ONE_SECOND
			#self.window.set_title("stopwatch %s" % self.elapsed_time)
			self.time.set_text(str(self.elapsed_time))

		return True


	def toggle_time(self, widget, data=None):
		if (self.enabled):
			self.enabled = False
			self.button.set_label("Start")
		else:
			self.enabled = True
			self.button.set_label("Stop")

		return


if __name__ == "__main__":
	stopwatch = Stopwatch()
	gtk.main()

		
