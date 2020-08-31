import random
import sys

def attempt(random):
    length = len(random)
    guess_word = (list("-"*length))
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    try_ = []
    count = 8
    while count > 0:
        if "-" not in guess_word:
            print("You guessed the word!")
            print("You survived!")
            #  sys.exit()

        print("")
        print("".join(guess_word))
        word = input("Input a letter: ")

        if len(word) > 1:
            print("You should input a single letter")
            continue  # Single letter

        if word not in alphabet:
            print("It is not an ASCII lowercase letter")
            continue

        if word in try_:
            print("You already typed this letter")
            continue

        try_.append(word)

        if word in random:
            for i in range(length):
                if random[i] == word:
                    guess_word[i] = word
        else:
            print("No such letter in the word")
            count -= 1
    print("You are hanged!")


words = ['python', 'java', 'kotlin', 'javascript']
random = words[random.randrange(0, 4)]

print("H A N G M A N")

while True:
    print()
    print('Type "play" to play the game, "exit" to quit:', end='')
    play_ = input()

    if play_ == "play":
        attempt(random)
    elif play_ == "exit":
        sys.exit()
