import time
import sys
import multiprocessing
from itertools import cycle
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, \
    QMainWindow, QPushButton, QAction


class Signal:
    go = True


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Reganto")
        self.setWindowIcon(QIcon("pic.png"))
        # actions 
        quit_action = QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("quit programm")
        quit_action.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quit_action)

        self.home()

    def home(self):
        btn = QPushButton("quit", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        self.show()

    def close_application(self):
        Signal.go = False
        sys.exit()
        

def run():
    app = QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())


def spin():
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in cycle("|/-\\"):
        write(char)
        flush()
        time.sleep(0.1)
        # \x08 is backspace
        write("\x08" * len(char))


def main():
    process1 = multiprocessing.Process(target=run)
    process2 = multiprocessing.Process(target=spin)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    if not Signal.go:
        process2.terminate()
    

main()
