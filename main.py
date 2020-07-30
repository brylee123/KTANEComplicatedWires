import complicatedwires
import maze
import morse
import passwords
import simplewires
import wiresequence

def menuoption(s):
	while True:
		try:
			choice = int(input(s))
			return choice
		except ValueError:
			print("Not a valid float. Try again.")

if __name__ == '__main__':
	while True:
		mainmenu =  """
					1. Complicated Wires
					2. Maze
					3. Morse
					4. Passwords
					5. Simple Wires
					6. Wire Sequence
					"""
		print(mainmenu)
		option = menuoption("Make a Selection: ")
		if option < 1 or option > 6:
			print("Invalid Selection. Try Again.")
			continue
		
		if option == 1:
			complicatedwires.complicatedwires()
		elif option == 2:
			maze.maze()
		elif option == 3:
			morse.morse()
		elif option == 4:
			passwords.passwords()
		elif option == 5:
			simplewires.simplewires()
		elif option == 6:
			wiresequence.wiresequence()

		
