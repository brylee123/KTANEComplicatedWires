def complicatedwires():

	serial_input = ""
	parallel_input = ""
	batteries_input = ""

	serial = False
	parallel = False
	batteries = False

	while not serial_input.isnumeric() or int(serial_input) > 2 or int(serial_input) < 1:
		serial_input = input("Is last digit of serial number even?\n\t1. Yes   2. No\n")
	if serial_input == "1":
		serial = True
	else:
		serial = False

	while not parallel_input.isnumeric() or int(parallel_input) > 2 or int(parallel_input) < 1:
		parallel_input = input("Is there a parallel port?\n\t1. Yes   2. No\n")
	if parallel_input == "1":
		parallel = True
	else:
		parallel = False

	while not batteries_input.isnumeric() or int(batteries_input) > 2 or int(batteries_input) < 1:
		batteries_input = input("Are there 2+ batteries?\n\t1. Yes   2. No\n")
	if batteries_input == "1":
		batteries = True
	else:
		batteries = False

	wire_number = 1
	while wire_number <= 6:
		star_input = ""
		led_input = ""
		color_input = ""

		star = False
		led = False

		print("====================================")
		print("Working on wire #"+str(wire_number))
		while not led_input.isnumeric() or int(led_input) > 2 or int(led_input) < 1:
			led_input = input("Is there an LED?\n\t1. Yes   2. No\n")
		if led_input == "1":
			led = True
		else:
			led = False

		while not color_input.isnumeric() or int(color_input) > 4 or int(color_input) < 1:
			color_input = input("Which of the following colors does the wire contain?\n\t1. red   2. blue   3. both   4. neither\n")
		color_input = int(color_input)

		while not star_input.isnumeric() or int(star_input) > 2 or int(star_input) < 1:
			star_input = input("Is there a star?\n\t1. Yes   2. No\n")
		if star_input == "1":
			star = True
		else:
			star = False

		# Logical comparison

		if color_input == 1: # Red
			if (batteries and led) or (star and not led) or (serial and not star and not led):
				print("Cut wire #"+str(wire_number))
			else:
				print("Do NOT cut wire #"+str(wire_number))

		elif color_input == 2: # Blue
			if (led and parallel) or (serial and not led and not star):
				print("Cut wire #"+str(wire_number))
			else:
				print("Do NOT cut wire #"+str(wire_number))

		elif color_input == 3: # Both
			if (not star and serial) or (star and not led and parallel):
				print("Cut wire #"+str(wire_number))
			else:
				print("Do NOT cut wire #"+str(wire_number))

		elif color_input == 4: # Neither
			if (not led) or (led and star and batteries):
				print("Cut wire #"+str(wire_number))
			else:
				print("Do NOT cut wire #"+str(wire_number))

		wire_number += 1

if __name__ == '__main__':
	complicatedwires()