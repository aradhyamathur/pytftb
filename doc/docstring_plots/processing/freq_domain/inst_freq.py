#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""

"""


import matplotlib.pyplot as plt
from tftb.processing.api import inst_freq
from tftb.generators.api import fmsin

x = fmsin(70, 0.05, 0.35, 25)[0]
instf, timestamps = inst_freq(x)
plt.plot(timestamps, instf)
plt.xlim(0, 70)
plt.grid()
plt.title("Instantaneous frequency estimation")
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()