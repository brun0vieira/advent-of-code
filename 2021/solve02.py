commands = [(command[0], int(command[1])) for line in open('input02.txt') if (command := line.strip().split(' '))]

horizontal, depth = 0, 0 

for command, value in commands:
	if command == 'forward':
		horizontal += value
	elif command == 'down':
		depth += value
	elif command == 'up':
		depth -= value

print(horizontal*depth)

horizontal, depth, aim = 0, 0, 0

for command, value in commands:
	if command == 'forward':
		horizontal += value
		depth += aim*value
	elif command == 'down':
		aim += value
	elif command == 'up':
		aim -= value

print(horizontal*depth)
