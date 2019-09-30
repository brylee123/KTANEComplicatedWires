def wiresequence():

	red_rules =   ["c", "b", "a", "ac", "b", "ac", "abc", "ab", "b"]
	blue_rules =  ["b", "ac", "b", "a", "b", "bc", "c", "ac", "a"]
	black_rules = ["abc", "ac", "b", "ac", "b", "bc", "ab", "c", "c"]

	wire_number = 1
	while wire_number <= 12:
		print("Configuring wire #", wire_number)
		color_input = ""
		while not color_input.isnumeric() or int(color_input) > 3 or int(color_input) < 1:
			color_input = input("Wire color:\n\t1. red   2. blue   3. black\n\t")
		color = int(color_input)

		connection_input = "x"
		while connection_input.lower() not in "abc":
			connection_input = input("What letter is the wire going into?:\n\ta   b   c\n\t")
		connection = connection_input.lower()

		if color == 1: # Red
			if connection in red_rules.pop(0):
				print("Conclusion: Cut wire")
			else:
				print("Conclusion: Do NOT cut wire")

		elif color == 2: # Blue
			if connection in blue_rules.pop(0):
				print("Conclusion: Cut wire")
			else:
				print("Conclusion: Do NOT cut wire")

		elif color == 3: # Black
			if connection in black_rules.pop(0):
				print("Conclusion: Cut wire")
			else:
				print("Conclusion: Do NOT cut wire")

		wire_number += 1

if __name__ == '__main__':
	wiresequence() 