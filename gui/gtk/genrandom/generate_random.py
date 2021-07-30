#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from uuid import uuid4
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title(title='Random')
        self.set_default_size(200, 10)
        
        box = Gtk.Box()
        box.set_spacing(spacing=6)
        self.add(box)

        btn = Gtk.Button.new_with_mnemonic(label='Ge_nerate')
        btn.connect('clicked', self.on_btn_clicked)
        box.pack_start(child=btn, expand=True, fill=True, padding=0)

        self.entry = Gtk.Entry()
        box.pack_start(child=self.entry, expand=True, fill=True, padding=0)

    def on_btn_clicked(self, button):
        self.entry.set_text(text=uuid4().hex[:8])
        

def supervisor():
    window = MyWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    supervisor()
