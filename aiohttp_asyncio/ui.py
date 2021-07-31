#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import requests


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title(title='Program')
        self.set_default_size(width=500, height=20)
        self.set_border_width(border_width=10)

        self.box = Gtk.Box()
        self.add(self.box)

        # entry and submit button
        self.box1 = Gtk.Box()
        self.box.pack_start(self.box1, True, True, 0)

        self.entry = Gtk.Entry()
        self.entry.set_text('Enter url here..')
        self.box1.pack_start(self.entry, True, True, 0)

        btn = Gtk.Button()
        btn.set_label(label='Submit')
        btn.connect('clicked', self.on_submit_clicked)
        self.box1.pack_start(btn, True, True, 0)


        # http request type (get | post) radio buttons
        self.box2 = Gtk.Box()
        self.box.pack_start(self.box2, True, True, 0)

        self.radio_btn = Gtk.RadioButton()
        self.radio_btn.set_label(label='Get')
        self.box2.pack_start(self.radio_btn, True, True, 0)

        self.radio_btn = Gtk.RadioButton()
        self.radio_btn.set_label(label='Post')
        self.box2.pack_start(self.radio_btn, True, True, 0)


        # parameters
        self.box3 = Gtk.Box()
        self.box.pack_start(self.box3, True, True, 0)

        entry1 = Gtk.Entry()
        entry2 = Gtk.Entry()
        entry1.set_text('parameter')
        entry2.set_text('value')
        
        self.box3.pack_start(entry1, True, True, 0)
        self.box3.pack_start(entry2, True, True, 0)
        # btn = Gtk.Button()
        # btn.set_label(label='click')
        # btn.connect('clicked', self.on_btn_clicked)
        # self.box.pack_start(btn, False, False, 0)

    # def on_btn_clicked(self, button):
    #     Gtk.main_quit()

    def on_submit_clicked(self, button):
        url = self.entry.get_text()
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as exc:
            print('Error -> ',exc)
        except requests.exceptions.HTTPError as exc:
            print('Error -> ',exc)
        except requests.exceptions.MissingSchema as exc:
            print('Error -> ',exc)
        else:
            response = response.json()



window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
