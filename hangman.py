import random

words = [line.strip() for line in open('sanalista.txt', 'r', encoding='utf-8')]  # opens sanalista.txt in utf-8-encoding
hangman = ['', '|', '|-', '|--', '|---', '|----', '|----o', '|----o|', '|----o|-', '|----o|-<']  # printable hangmen

# Returns a random word from file sanalista.txt
def randomWord(wordList):
    index = random.randint(0, len(wordList) - 1)  # takes a random word from sanalista.txt
    return wordList[index]  # returns the random word - that's how return works

# Prints the status of the game
def hangmanGame(correctWord, hangman, missed, letters, points):
    print()
    print('Oikeat kirjaimet:', letters)
    print('Väärät kirjaimet:', missed)
    print(hangman[points])

    spaces = '_ ' * len(correctWord)  # writes as many underscores as there are chars in correctWord
    for i in range(len(correctWord)):  # replaces spaces with correct letters
        if correctWord[i] in letters:
            i2 = i * 2
            spaces = spaces[:i2] + correctWord[i] + spaces[i2 + 1:]  # replaces the i:th char with letter

    print(spaces, end=' ')  # Prints the current progress

# Player gives a guess and the function validates it. Returns one or more lowercase characters
def getGuess(alreadyGuessed, correctLength):
    while True:
        guess = input('\nArvaa kirjain: ').lower()
        if len(guess) == 1:
            if guess in alreadyGuessed:
                print('Olet arvannut jo tämän kirjaimen!')
            elif guess not in 'abcdefghijklmnopqrstuvwxyzåäö':
                print('Ole hyvä ja syötä kirjain.')
            else:
                return guess
        elif len(guess) == correctLength:
            return guess
        else:
            print("Väärän mittainen arvaus!")

# Plays one round of hangman
def runGame():
    correctWord = randomWord(words)  # The answer word
    letters = ''  # Correctly guessed letters
    missed = ''  # Incorrectly guessed letters
    points = 0  # Counting wrong guesses
    gameRunning = True

    while gameRunning:  # Loops until the round has been won or lost
            hangmanGame(correctWord, hangman, missed, letters, points)

            guess = getGuess(missed + letters, len(correctWord))
            # checks if the was correct
            if len(guess) == 1:
                if guess in correctWord:
                    letters += guess
                else:
                    missed += guess
                    points += 1
            else:
                if guess == correctWord:
                    letters += '@'  # This is just for counting right guesses
                else:
                    print("Arvauksesi on väärä!")
                    points += 1
            if points == len(hangman) - 2:
                print("\nViimeinen arvaus!")

            # Checks if the game has been won
            allLetters = True
            if guess != correctWord:
                for i in range(len(correctWord)):
                    if correctWord[i] not in letters:
                        allLetters = False
                        break
            if allLetters:
                print("\nOnnea! Voitit pelin!", end=" ")
                gameRunning = False

            # Checks if the game has been lost
            if points == len(hangman) - 1:
                hangmanGame(correctWord, hangman, missed, letters, points)
                print("\nHirteen jouduit!", end=" ")
                gameRunning = False
            
    translation = ['kerran', 'kertaa'] # False evaluates to 0, True to 1. Use these as array indices
    print("Arvasit väärin", points, translation[(points != 1)], "ja oikein", len(letters), translation[(len(letters) != 1)] + ". Oikea sana oli", correctWord + ".")

gameStatus = True
print("Kitin hirsipuupeli")
while gameStatus == True:
    print("================\n")
    print('Pelataan hirsipuuta!')
    runGame()

    playerStatus = input("Haluatko pelata uudelleen? Kirjoita kyllä jos haluat pelata uudelleen: ").lower()
    if playerStatus not in ["kyllä", "joo", "okei", "yes", "k", "y"]:
        print("\nKiitos pelistä!")
        gameStatus = False
