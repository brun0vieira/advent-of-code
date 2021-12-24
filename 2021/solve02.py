#!/usr/bin/env python3

import numpy as np

measurements = [int(m) for m in open('input01.txt')]
windows = np.convolve(measurements, np.ones(3), 'valid')

print(np.sum(np.diff(windows) > 0))
