def simplewires():

	black = False
	blue = False
	red = False
	white = False
	yellow = False

	wire = {
		1: "black",
		2: "blue",
		3: "red",
		4: "white",
		5: "yellow"
	}

	sequence = []
	current_wire = ""
	while len(sequence) <= 6:
		while not current_wire.isnumeric() or int(current_wire) > 6:
			current_wire = input("What color is this wire?\n\t1. black   2. blue   3. red   4. white   5. yellow   6. done")
		if current_wire == "6":
			break
		sequence.append(wire[current_wire])

	if len(sequence) == 3:
		if "red" not in sequence:
			print("Cut second wire")
		elif sequence[-1] == "white":
			print("Cut last wire")
		elif sequence.count("blue") > 1:
			print("Cut last blue wire")
		else:
			print("Cut last wire")

	elif len(sequence) == 4:
		if sequence.count("red") > 1:
			serial = ""
			odd = False
			while not serial.isnumeric() or int(serial) > 2:
				serial = input("Is the last digit of the serial number odd?\n\t1. yes   2. no")
			if serial == "1":
				print("Cut last wire")
		elif sequence[-1] == "yellow" and sequence.count("red") == 0:
			print("Cut first wire")
		elif sequence.count("blue") == 1:
			print("Cut first wire")
		elif sequence.count("yellow") > 1:
			print("Cut last wire")
		else:
			print("Cut second wire")

	elif len(sequence) == 5:
		if sequence[-1] == "black":
			serial = ""
			while not serial.isnumeric() or int(serial) > 2:
				serial = input("Is the last digit of the serial number odd?\n\t1. yes   2. no")
			if serial == "1":
				print("Cut fourth wire")
		elif sequence.count("red") == 1 and sequence.count("yellow") > 1:
			print("Cut first wire")
		elif "black" not in sequence:
			print("Cut second wire")
		else:
			print("Cut first wire")

	elif len(sequence) == 6:
		if "yellow" not in sequence:
			serial = ""
			while not serial.isnumeric() or int(serial) > 2:
				serial = input("Is the last digit of the serial number odd?\n\t1. yes   2. no")
			if serial == "1":
				print("Cut third wire")
		elif sequence.count("yellow") == 1 and sequence.count("white") > 1:
			print("Cut fourth wire")
		elif "red" not in sequence:
			print("Cut last wire")
		else:
			print("Cut fourth wire")

if __name__ == '__main__':
	simplewires()