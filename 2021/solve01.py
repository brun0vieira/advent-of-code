measurements = []
count = 0

with open('input1.txt') as file:
	for line in file:
		measurements.append(int(line.rstrip()))

for i in range(len(measurements) - 1):
	if measurements[i+1] > measurements[i]:
		count += 1

print(count)
