import re
# Format string to remove all non-alphabet characters and spaces, and convert to lowercase
# Add letters to a set and count the result. If the set has 26 items, the phrase is a pangram.

def is_pangram(phrase):
	alphabet = set()
	phrase = re.sub("[^a-zA-Z]", "", phrase)
	phrase = phrase.lower()
	for letter in phrase:
		alphabet.add(letter)
	
	if len(alphabet) == 26:
		return True
	else:
		return False

