#!/usr/bin/env python
#
# A trivial little stopwatch application.  Useful for tracking 'billable time',
# and 'how long have I wasted on ...' sorts of things.
#
# Usage:
#    % python stopwatch.py
#

import datetime
import sys

import pygtk
pygtk.require("2.0")
import gtk
import gobject


ONE_SECOND = datetime.timedelta(seconds=1)


class Stopwatch(object):
	def __init__(self):
		# The actual stopwatch/time content
		self.enabled = False
		self.elapsed_time = datetime.timedelta()

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

		# Window layout: elapsed time counter on top; buttons beneath
		vbox = gtk.VBox(True, 0)

		# ... the actual time display ...
		self.time_counter = gtk.Label(str(self.elapsed_time))
		self.time_counter.set_width_chars(8)	# "hh:mm:ss"
		vbox.pack_start(self.time_counter, True, True, 0)
		self.time_counter.show()

		hbox = gtk.HBox(True, 0)
		vbox.pack_start(hbox, True, True, 0)

		# ... start/stop toggle button ...
		self.toggle_button = gtk.Button("Start")
		self.toggle_button.connect("clicked", self.toggle_time)
		hbox.pack_start(self.toggle_button, True, True, 0)
		self.toggle_button.show()

		# ... and a reset button
		reset_button = gtk.Button("Reset")
		reset_button.connect("clicked", self.reset_time)
		hbox.pack_start(reset_button, True, True, 0)
		reset_button.show()

		hbox.show()
		vbox.show()
		self.window.add(vbox)

		return


	def destroy(self, widget, data=None):
		"""Window deletion callback.  Close the application"""
		gtk.main_quit()


	def refresh_time(self):
		"""Update the elapsed time display.  Invoked once per second"""
		if (self.enabled):
			self.elapsed_time += ONE_SECOND
			#self.window.set_title("stopwatch %s" % self.elapsed_time)
			self.time_counter.set_text(str(self.elapsed_time))

		return True


	def reset_time(self, widget, data=None):
		"""
		Reset the elapsed time back to zero.  Invoked when the reset
		button is pressed.
		"""
		self.elapsed_time = datetime.timedelta()
		self.time_counter.set_text(str(self.elapsed_time))
		return


	def toggle_time(self, widget, data=None):
		"""
		Start or stop the stopwatch, as appropriate.  Invoked when the
		start/stop button is pressed.
		"""
		if (self.enabled):
			self.enabled = False
			self.toggle_button.set_label("Start")
		else:
			self.enabled = True
			self.toggle_button.set_label("Stop")

		return


if __name__ == "__main__":
	stopwatch = Stopwatch()
	gtk.main()
	sys.exit(0)

		
