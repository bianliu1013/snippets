#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Plot a 2D histogram

See:

- http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut3.html
"""

import numpy as np
import matplotlib.pyplot as plt

# MAKE DATA ###################################################################

x, y = np.random.normal(size=(2, 100000))

# INIT FIGURE #################################################################

fig = plt.figure(figsize=(8.0, 8.0))
ax = fig.add_subplot(111)

# AX ##########################################################################

H = ax.hist2d(x, y, bins=40)
fig.colorbar(H[3], ax=ax)

# SHOW AND SAVE FILE ##########################################################

plt.tight_layout()

plt.savefig("hist2d.png")
plt.show()
