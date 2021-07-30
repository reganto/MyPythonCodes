#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os


class MyWindow(Gtk.Window):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.set_title('stat')
        self.set_default_size(300, 20)

        box = Gtk.Box()
        box.set_spacing(6)
        self.add(box)

        self.entry = Gtk.Entry()
        box.pack_start(self.entry, True, True, 0)

        stat_btn = Gtk.Button.new_with_mnemonic('_Stat')
        stat_btn.connect('clicked', self.on_stat_btn)
        box.pack_start(stat_btn, True, True, 0)

        # self.text_entry = Gtk.Entry()
        # box.pack_start(self.text_entry, True, True, 0)

    def on_stat_btn(self, button):
        path = self.entry.get_text()
        try:
            if os.path.isfile(path):
                raise ('enter a folder')
            else:
                st = os.stat(path)
            
            self.entry.set_text(st)

        except :
            self.entry.set_placeholder_text('Enter folder path')


window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
