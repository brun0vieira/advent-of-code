measurements = []
count = 0

with open('input01.txt') as file:
	for line in file:
		measurements.append(int(line.rstrip()))

for i in range(len(measurements) - 1):
	if measurements[i+1] > measurements[i]:
		count += 1

print(count)

import numpy as np 

measurements = [int(m) for m in open('input01.txt')]
windows = np.convolve(measurements, np.ones(3), 'valid')

print(np.sum(np.diff(windows) > 0))

