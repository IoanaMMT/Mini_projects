import time

user_name = input("What is your name?")
print("Hello " + user_name + "!" )
time.sleep(1.5)
print("This is a password generator. Please enter 3 words and we will give you the password")
time.sleep(1.5)

# Collecting the words for the password

word1 = input("First word: ")
word2 = input("Second word: ")
word3 = input("Third word: ")


#The function that picks up the first 3 letters of the word
def generator(word):
    for i in word:
        first_letters = word[0:3]
    return first_letters

subject1 = generator(word1)
subject2 = generator(word2)
subject3 = generator(word3)

password = (subject1 + subject2 + subject3 + str(len(word1 + word2 + word3)))
print("Your password is: " + password)
