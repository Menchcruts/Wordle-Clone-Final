import random

from functions import fileToList, clearTerminal
from mainFuncs import drawBoard, evaluteGuess
from rowClass import Letter

def main(randomWord):

    validWords = fileToList("valid-wordle-words2.txt")
  
    if randomWord:
        secretWord = random.choice(validWords)
    else:
        secretWord = "chode"
    

    #Create the inital board with empty boxes
    board = {}
    for i in range(1,7):
        letterList = []
        for x in range(5):
            letterList.append(Letter())
    
        board[i] = letterList
    

    playing = True
    gaveUp = False
    won = False
    guessNumber = 1
    
    while playing:
        clearTerminal()
        drawBoard(board)
        
        if guessNumber > 6 or won:
            playing = False
            break
        
        guess = input().lower()
        guess = guess.replace(" ","")
        
        if guess == "#quit":
            playing = False
            gaveUp = True
            print("You gave up")
            break
        
        won = bool(guess == secretWord)
        
        if guess in validWords:
            if len(guess) == 5:
                board[guessNumber] = evaluteGuess(guess, board[guessNumber], secretWord)
                guessNumber += 1
        
            elif len(guess) > 5:
                print("Guess too long.")
                input("Please press enter to guess again\n")
        
            else:
                print("Guess too short.")
                input("Please press enter to guess again\n")
        else:
            print("Word not found!")
            input("Please press enter to guess again\n")
            

        

    #Outside play loop
    if won:
        print(f"You guessed the word in {guessNumber-1} guesses.")
        print(f"The word was {secretWord.title()}")
        return 1
    else:
        if not gaveUp:
            print("You ran out of guesses. Bummer.")
        print(f"The word was {secretWord.title()}")
        return 0