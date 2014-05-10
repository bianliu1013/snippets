#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Debian packages required:
# - python-poppler-qt4  (not python-poppler)

# See: http://stackoverflow.com/questions/10562945/how-to-display-pdf-with-python-poppler-qt4
#      http://web.archive.org/web/20120417095851/http://www.rkblog.rk.edu.pl/w/p/rendering-pdf-files-pyqt4-pypoppler-qt4/
#      http://bazaar.launchpad.net/~j-corwin/openlp/pdf/annotate/head:/openlp/plugins/presentations/lib/pdfcontroller.py


import sys
import argparse

from PyQt4 import QtGui, QtCore

import popplerqt4

class PDFController():
    # TODO
    def __init__(self, window_slides, window_notes):
        pass

class Window(QtGui.QWidget):
    def __init__(self, name, doc):
        super(Window, self).__init__()

        self.doc = doc

        self.current_page_num = 0
        self.num_pages = self.doc.numPages()

        # Create a label with the pixmap
        self.label = QtGui.QLabel(self)

        # Create the layout
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.label)

        # Set the layout
        self.setLayout(vbox)

        self.resize(800, 600)
        self.setWindowTitle(name)
        self.show()

    def updatePixmap(self):
        page = self.doc.page(self.current_page_num)

        if page is not None:
            # See http://people.freedesktop.org/~aacid/docs/qt4/classPoppler_1_1Page.html
            # page.renderToImage(xres=72.0, yres=72.0, x=-1, y=-1, width=-1, height=-1, rotate)
            # 
            # Parameters
            #   x   specifies the left x-coordinate of the box, in pixels.
            #   y   specifies the top y-coordinate of the box, in pixels.
            #   w   specifies the width of the box, in pixels.
            #   h   specifies the height of the box, in pixels.
            #   xres    horizontal resolution of the graphics device, in dots per inch
            #   yres    vertical resolution of the graphics device, in dots per inch
            #   rotate  how to rotate the page
            #image = page.renderToImage(300.0, 300.0, -1, -1, -1, -1)
            image = page.renderToImage()
            pixmap = QtGui.QPixmap.fromImage(image)

            self.label.setPixmap(pixmap)
            self.label.resize(self.label.sizeHint())


    def keyPressEvent(self, e):
        # See http://pyqt.sourceforge.net/Docs/PyQt4/qt.html#Key-enum for all keys
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        elif e.key() == QtCore.Qt.Key_Return:
            self.current_page_num = min(self.current_page_num + 1, self.num_pages - 1)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Space:
            self.current_page_num = min(self.current_page_num + 1, self.num_pages - 1)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_PageUp:
            self.current_page_num = min(self.current_page_num + 5, self.num_pages - 1)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_PageDown:
            self.current_page_num = max(self.current_page_num - 5, 0)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Home:
            self.current_page_num = 0
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_End:
            self.current_page_num = self.num_pages - 1
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Left:
            self.current_page_num = max(self.current_page_num - 1, 0)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Right:
            self.current_page_num = min(self.current_page_num + 1, self.num_pages - 1)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Up:
            self.current_page_num = min(self.current_page_num + 1, self.num_pages - 1)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Down:
            self.current_page_num = max(self.current_page_num - 1, 0)
            self.updatePixmap()

        elif e.key() == QtCore.Qt.Key_Tab:
            # Switch screen
            # TODO
            pass

def main():
    """Main function"""

    # PARSE OPTIONS ###################

    parser = argparse.ArgumentParser(description='PDF Presenter Dual Head.')

    parser.add_argument("--notes", "-n",  help="Notes (PDF files)", metavar="FILE")
    parser.add_argument("fileargs", nargs=1, metavar="FILE", help="Slides (PDF file)")

    args = parser.parse_args()

    # TODO: test arguments

    # POPPLER #########################

    slides_doc = popplerqt4.Poppler.Document.load(args.fileargs[0])
    slides_doc.setRenderHint(popplerqt4.Poppler.Document.Antialiasing and popplerqt4.Poppler.Document.TextAntialiasing)

    notes_doc = popplerqt4.Poppler.Document.load(args.notes)
    notes_doc.setRenderHint(popplerqt4.Poppler.Document.Antialiasing and popplerqt4.Poppler.Document.TextAntialiasing)

    # QT4 #############################

    app = QtGui.QApplication(sys.argv)

    # For an application, the screen where the main widget resides is the
    # primary screen. This is stored in the primaryScreen property. All windows
    # opened in the context of the application should be constrained to the
    # boundaries of the primary screen; for example, it would be inconvenient
    # if a dialog box popped up on a different screen, or split over two
    # screens.
    desktop = QtGui.QDesktopWidget()

    #print(desktop.numScreens())
    #print(desktop.primaryScreen())

    # The default constructor has no parent.
    # A widget with no parent is a window.
    window_slides = Window("PDF Presenter (Slides)", slides_doc)
    window_notes = Window("PDF Presenter (Notes)", notes_doc)

    qrect0 = desktop.screenGeometry(0)
    qrect1 = desktop.screenGeometry(1)

    window_slides.move(qrect0.left(), qrect0.top())
    window_notes.move(qrect1.left(), qrect1.top())

    window_slides.showFullScreen()
    window_notes.showFullScreen()

    # The mainloop of the application. The event handling starts from this point.
    # The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead. 
    exit_code = app.exec_()

    # The sys.exit() method ensures a clean exit.
    # The environment will be informed, how the application ended.
    sys.exit(exit_code)

if __name__ == '__main__':
    main()


