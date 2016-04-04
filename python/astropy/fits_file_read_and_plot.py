#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Documentation: http://docs.astropy.org/en/stable/io/fits/index.html

import argparse
from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# PARSE OPTIONS ###############################################################

parser = argparse.ArgumentParser(description="An astropy snippet")

parser.add_argument("filearg", nargs=1, metavar="FILE", help="the FITS file to process")

args = parser.parse_args()

file_path = args.filearg[0]


# READ DATA ###################################################################

# Open the FITS file
hdu_list = fits.open(file_path)

# Print the content of the FITS file (HDU headers)
hdu_list.info()

print("---")

for hdu_id, hdu in enumerate(hdu_list):
    print("HDU {}".format(hdu_id))

    header = hdu.header
    for key, value in header.items():
        print(key, ":", value)

    print("---")

    data = hdu.data   # "hdu.data" is a Numpy Array

    if data.ndim == 2:
        # If there is only one image (data is an 2D array)
        fig = plt.figure(figsize=(8.0, 8.0))
        ax = fig.add_subplot(111)

        ax.imshow(data, interpolation='nearest', cmap=cm.gray)
        ax.set_title("HDU {}".format(hdu_id))

        plt.savefig("HDU{}.png".format(hdu_id))

        plt.show()
    elif data.ndim == 3:
        # If there are more than one image (data is an 3D array)
        for img_index, img in enumerate(data):
            fig = plt.figure(figsize=(8.0, 8.0))
            ax = fig.add_subplot(111)

            ax.imshow(img, interpolation='nearest', cmap=cm.gray)
            ax.set_title("HDU {} {}".format(hdu_id, img_index))

            plt.savefig("HDU{}_{}.png".format(hdu_id, img_index))

            plt.show()

# Close the FITS file
hdu_list.close()

