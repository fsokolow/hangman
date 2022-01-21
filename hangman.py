# Write your code here
import random

play = True
print("H A N G M A N")
while play:
    play_or_exit = input('Type "play" to play the game, "exit" to quit:')
    if play_or_exit == 'play':
        word_list = ['python', 'java', 'kotlin', 'javascript']
        guess = random.choice(word_list)
        word_letters = set(guess)
        printed = list('-' * len(guess))
        checked = set()
        lives = 8
        while lives > 0:
            if guess == "".join(printed):
                print()
                print(guess, "\nYou guessed the word!\nYou survived!")
                print()
                break
            print()
            print(''.join(printed))
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            elif letter.isalpha() is False or letter.isupper():
                print("Please enter a lowercase English letter")
                continue
            elif letter in word_letters:
                start = 0
                if letter in checked:
                    print("You've already guessed this letter")
                    continue
                for j in range(guess.count(letter)):
                    printed[guess.index(letter, start)] = letter
                    start = guess.index(letter, start) + 1
                checked.add(letter)
            else:
                if letter in checked:
                    print("You've already guessed this letter")
                    continue
                print("That letter doesn't appear in the word")
                checked.add(letter)
                lives -= 1
        else:
            print("You lost!")
            print()
    elif play_or_exit == "exit":
        play = False
