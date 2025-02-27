import random
word_list = ["apple", "kiwi", "banana", "dragonfruit", "pomegranite"]
word = random.choice(word_list)
print(word)
guess = str(input("Please choose a letter. "))
if len(guess)==1:
	print("Good guess!")
else:
	print("Oops, that is not a valid input.")
