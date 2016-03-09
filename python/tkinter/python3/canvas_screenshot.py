#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

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

# See also: http://effbot.org/tkinterbook/widget.htm
#           http://effbot.org/tkinterbook/canvas.htm

import tkinter as tk
import os
import os.path

SIZE = 250

FPS = 100
TIME_STEP_MS = int(1000 / FPS)

SCREENCAST_PATH = "."
SCREENCAST_ITERATION = 0

def main():
    """Main function"""

    root = tk.Tk()

    canvas = tk.Canvas(root, width=SIZE, height=SIZE, background="white")
    canvas.pack()

    # Draw the ball
    coordinates = (0, int(SIZE/2)-25, 50, int(SIZE/2)+25)
    ball = canvas.create_oval(coordinates, fill="red", width=2)

    def update_canvas():
        # Update the ball's coordinates
        coordinates = canvas.coords(ball)    # Get the ball's coordinates
        coordinates[0] = (coordinates[0] + 1) % SIZE
        coordinates[2] = coordinates[0] + 50

        # Redraw the ball
        canvas.coords(ball, *coordinates)    # Set the ball's coordinates

        # Take a screenshot and save it into a file.
        global SCREENCAST_ITERATION
        SCREENCAST_ITERATION += 1
        basename = os.path.join(SCREENCAST_PATH, '%05d' % SCREENCAST_ITERATION)

        canvas.postscript(file=basename + '.ps', colormode='color')  # Make the screenshot

        # The following commands can be used to convert PS files to JPEG or PNG on Unix platforms
        #if SCREENSHOT_FORMAT == 'jpeg':
        #    cmd = 'gs -sDEVICE=jpeg -dJPEGQ=100 -sOutputFile=%(bn)s.%(format)s -dGraphicsAlphaBits=4 -dTextAlphaBits=4 -dEPSCrop -dNOPAUSE -q -dBATCH %(bn)s.ps' % {'bn': basename, 'format': SCREENSHOT_FORMAT}
        #else:
        #    # PNG DEVICES : pngalpha png16m pnggray png256 png16 pngmono
        #    cmd = 'gs -sDEVICE=png16m -sOutputFile=%(bn)s.%(format)s -dGraphicsAlphaBits=4 -dTextAlphaBits=4 -dEPSCrop -dNOPAUSE -q -dBATCH %(bn)s.ps' % {'bn': basename, 'format': SCREENSHOT_FORMAT}
        #os.system(cmd)

        # Reschedule event in TIME_STEP_MS milli second
        root.after(TIME_STEP_MS, update_canvas)

    # Schedule event in TIME_STEP_MS milli second
    root.after(TIME_STEP_MS, update_canvas)

    root.mainloop()

if __name__ == '__main__':
    main()
