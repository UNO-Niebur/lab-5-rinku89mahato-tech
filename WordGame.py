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
    correctletter = word[spot]
    if letter == correctLetter:
        return True
    else: 
        return False

    

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback =""

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
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    guessNum = 1
    while guessNum <= 6:
        #Ask user for their guess
        validWord = False
        while validWord == False:
            guess = input("What is your guess: ")
            guess = guess.lower()
            if guess not in wordList:
                print("Word not in list.")
                validWord = False
            else:
                validWord = True

    #Give feedback using on their word:
    feedback = rateGuess(guess, todayWord)
    print(feedback)
    if feedback == todayWord.upper():
        print("You got it in", guessNum, "tries!")
        break
    
    guessNum = guessNum +1


print("The word was", todayWord)






if __name__ == '__main__':
  main()
