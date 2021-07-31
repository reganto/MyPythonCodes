#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import uuid
import sys
import itertools
import time
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title('Random')
        self.set_default_size(200, 10)

        box = Gtk.Box(spacing=6)
        self.add(box)

        btn = Gtk.Button.new_with_mnemonic('Ge_nerate')
        btn.connect('clicked', self.on_btn_clicked)
        box.pack_start(child=btn, expand=True, fill=True, padding=0)

        self.entry = Gtk.Entry()
        box.pack_start(child=self.entry, expand=True, fill=True, padding=0)

    def on_btn_clicked(self, button):
        self.entry.set_text(uuid.uuid4().hex[:8])


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


def make_window():
    window = MyWindow()
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()


@asyncio.coroutine
def delay():
    yield from asyncio.sleep(3)
    return 10


@asyncio.coroutine
def enumate():
    for i in range(10):
        print(i)
        yield from asyncio.sleep(1)


@asyncio.coroutine
def supervisor():
    task1 = asyncio.Task(spin('loading..'))
    task2 = asyncio.Task(enumate())
    result = delay()
    make_window()
    task1.cancel()
    task2.cancel()    


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(supervisor())
    loop.close()
    

if __name__ == "__main__":
    main()
