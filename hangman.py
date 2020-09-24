
import time
from random_word import RandomWords

name = input("What is your name?")

print ("Hello {} time to play Hangman!\n".format(name))

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

r = RandomWords()

word = r.get_random_word()

guesses = ''
turns = 10
l = list()
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won! You guessed {} correctly!".format(word))
        break
    print
    guess = input("Guess a character: ")
    guesses += guess
    
    if guess not in word:
        turns -= 1
        l.append(guess)
        print("Wrong")
        
        if turns == 0:
            print("You lose")
            print("The word was: {}".format(word))
    
    print("You have {} more lives".format(turns))
    print("You have guessed: {} incorrectly".format(l))
