def passwords():
	wordbank = {
		"about", "after", "again",
		"below",
		"could",
		"every",
		"first", "found",
		"great",
		"house",
		"large", "learn",
		"never",
		"other",
		"place", "plant", "point",
		"right",
		"small", "sound", "spell", "still", "study",
		"their", "there", "these", "thing", "think", "three",
		"water", "where", "which", "world", "would", "write"
	}

	candidates = wordbank.copy()
	
	for i in range(1,6): # 1-5

		column = ""
		while not column.isalpha() or len(column) != 6:
			column = input("Column"+str(i)+": ")
			column = "".join(set(column)).lower() # Remove duplicates
		
		for word in wordbank: # (35 comparisons)
			word_valid = False
			for letter in column: # (6 comparisons)
				if word[i-1] == letter:
					word_valid = True
			if not word_valid:
				candidates.remove(word)

		if len(candidates) == 1:
			print("The password is:", candidates.pop())
			break
		else:
			print("Possible password candidates are:", candidates)
		wordbank = candidates.copy()
	
if __name__ == '__main__':
	passwords()