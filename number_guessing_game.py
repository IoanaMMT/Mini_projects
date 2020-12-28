import random

num_list = range(10)

guesses = 0
correct_guesses = 0

while guesses < 10:
    try:
        n = random.randint(1, 10)
        user_input = int(input("Guess a number from 1 to 10: "))

        if user_input == n:
            print("well done")
            guesses += 1
            correct_guesses +=1
        elif user_input > 10:
            print(" Only numbers from 1 to 10")
        elif user_input > n:
            print("Too high")
            guesses += 1
        elif user_input < n:
            print("Too low")
            guesses += 1
    except ValueError:
        print("Error! Only numbers, please")

print("Guesses: " + str(guesses))
print("Corect guesses: " + str(correct_guesses))


print(n)

if correct_guesses >= 2:
    print("You won!")
else:
    print("Sorry, you lost!")
