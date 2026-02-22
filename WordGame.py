#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    else: 
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""

    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback +myLetter.upper() #correct letter in location
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower() # letter is in word, not correct spot
        else:
            feedback = feedback + "*"

    return feedback

def main():
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    worldlist = content.split("\n")
    todayword = random.choice(worldlist)
    print(todayword)

    #user should get 6 guesses to guess
    guessNum = 1
    while guessNum <= 6:
        #ask user for their guess
        validWord = False
        while validWord ==False:
            guess = input ("Enter guess: ")
            guess = guess.lower()
            if guess not in worldlist:
                print("word not in list.")
                validWord = False
            else:
                validWord = True
        #give feedback using on their word:
        feedback = rateGuess(guess, todayword)
        print(feedback)
        if feedback == todayword.upper():
            print("You got it in", guessNum, "tries!")
            break
        guessNum = guessNum + 1

    print("The word was", todayword)
    print("Bye")
    

if __name__ == '__main__':
    main()
  #pick a random word from list of all words
  #
  
