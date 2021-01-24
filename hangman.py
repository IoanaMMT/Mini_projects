import random

play_again = True

while play_again:
	words = ["heroic", "secretarial", "computer", "engineering",
 			"instructions", "machines", "development",
 			"frequently", "technicians", "programmed"
			]


	chosen_word = random.choice(words)
	user_guess = None
	split_chosen_word = []
	hiden_letters = []
	join_letters = None
	guessed_letters = []
	attempts = 10
	print(chosen_word)

	for i in chosen_word:
		split_chosen_word.append(i)

	for i in split_chosen_word:
		hiden_letters.append("-")
	

	for i in hiden_letters:
		join_letters = "".join(hiden_letters)
	print(join_letters)

	while "-" in hiden_letters and attempts > 0:
		try:
			user_guess = input(str("Guess a letter: "))
		except:
			if user_guess.isalpha():
				print("Sorry, it needs to be a letter. Try again")
				continue
			elif len(user_guess) > 1:
				print("Only one letter at the time. Try again")
				continue
			elif user_guess in guessed_letters:
				print("Letter already guessed. Try again")
				continue
			else:
				pass

		for letter in range(len(chosen_word)):
			if user_guess == chosen_word[letter]:
				hiden_letters[letter] = user_guess
			#elif user_guess not in chosen_word:
				#attempts -= 1
		#print("You have " + str(attempts) + " attempts left")

		for i in hiden_letters:
			join_letters = "".join(hiden_letters)
		print(join_letters)

