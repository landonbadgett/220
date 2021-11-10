"""
Name: <Landon Badgett>
<lab11>.py
"""

from random import *

wordList = "wordlist.txt"
def getWords(wordList):
    file = open(wordList, 'r')
    words = []
    for line in file:
        x = line[0:]
        words.append(x.strip())

    return words

def pickWord(words):
    position = randint(0, len(words))
    secret_word = words[position]
    return secret_word

def guessedWord(secret_word, guessed_letters, guessed_word, turn_count, letter):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False

def wordSpell(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    return False

def guessLetter(guessed_letters, turn_count, secret_word, guessed_word):
    letter = input("Enter a letter: ")
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            while letter == ch:
                letter = input("Already tried! Guess another letter: ")
                check = False
    return guessedWord(secret_word, guessed_letters, guessed_word, turn_count, letter)

def printBoard(guessed_word, turn_count, guessed_letters):
    print("----------------------------")
    print(guessed_word)
    print()
    print("Turn count: ", turn_count)
    print("Guessed Letters: ", guessed_letters)
    print("----------------------------")



def play_game():
    turn_count = 0
    secret_word = pickWord(getWords(wordList))
    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpell(guessed_word, secret_word):
        if guessLetter(guessed_letters, turn_count, secret_word, guessed_word) is False:
            turn_count += 1
            printBoard(guessed_word, turn_count, guessed_letters)
        else:
            printBoard(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("Game is over! You lose!")
    else:
        print("Congratulations! You won the game!")






















def main():
    play_game()
    pass


main()
