import random
word_list = ["apple", "banana", "cherry", "dragonfruit", "eggplant"]
word = random.choice(word_list)
while True:
	guess = input("Please guess a letter. ")
	if guess.isalpha():
		break
	else:
		print("Invalid letter. Please, enter a single alphabetical character.")
	for letter in word:
		if guess in word:
			print(f"Good guess, {guess} is in the word")
	else:
		print(f"Sorry, {guess} is not in the word. Try again.")

def check_guess(guess):
	guess.lower
