import hashlib
import random

account_exists = input("Do you have an account? (Y/N): ")
username = ''
password = ''
f = ''
if account_exists == 'Y':
    print("Continuing....")
elif account_exists == 'N':
    create_account = input("Would you like to create an account? (Y/N): ")
    if create_account == 'Y':
        username = input("Enter a username: ")
        username_save = open('usernames.txt', 'a')
        username_save.write(username)
        password = input("Enter a password: ")
        password1 = input("Please reenter your password: ")
        if password1 == password:
            with open("passwords.txt", "w")as f:
                hashed_password_object = hashlib.md5(password.encode())
                f.write(hashed_password_object.hexdigest())
                print("Thank you for creating an account!")
                print('Your account information has been stored. Please re-run JIM and select \"Y".')
                exit()
        elif password1 != password:
            print("Passwords don't match.")
            exit()

    elif create_account == 'N':
        print("Screw off then.")
        exit()


def google():
    google_search_ask = input("Great. What would you like to search for: ")
    google_search_ans = ""
    print(google_search_ans)


def hangman():
    hangman_pics = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       0   |
           |
           |
          ===''', '''
       +---+
       0   |
       |   |
           |
          ===''', '''
       +---+
       0   |
      /|   |
           |
          ===''', '''
       +---+
       0   |
      /|\  |
           |
          ===''', '''
       +---+
       0   |
      /|\  |
      /   |
          ===''', '''
       +---+
       0   |
      /|\  |
      / \  |
          ===''']
    words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

    def getRandomWord(wordList):
        wordIndex = random.randint(0, len(wordList) - 1)
        return wordList[wordIndex]

    def displayBoard(missedLetters, correctLetters, secretWord):
        print(hangman_pics[len(missedLetters)])
        print()

        print('Missed letters:', end=' ')
        for letter in missedLetters:
            print(letter, end=' ')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

        for letter in blanks:
            print(letter, end=' ')
        print()

    def getGuess(alreadyGuessed):
        while True:
            print('Guess a letter.')
            guess = input()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print("You have already guessed that letter. Please guess again.")
            elif guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a LETTER.")
            else:
                return guess

    def playAgain():
        print('Do you want to play again? (Y/N): ')
        return input().upper().startswith('Y')


    print('H A N G M A N')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundALLletters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundALLletters = False
                    break
            if foundALLletters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True

        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(hangman_pics) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' +
                      str(len(missedLetters)) + ' missed guesses and ' +
                      str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                main()

def main():
    google_search_q = input("Would you like JIM to search google (Y/N): ")
    if google_search_q == ("Y"):
        google()
    else:
        game_ask = input("If you would like to play a game (Y/N): ")
        if game_ask == ("Y"):
            hangman()



def login():
    login_password1 = ''
    username1 = input("My username is: ")
    print("Your username is " + username1)
    with open('usernames.txt') as x:
        if username1 in x.read():
            print("Account found.")
        elif username1 is not x.read():
            no_account = input("Account not found. Do you have an account? (Y/N): ")
            if no_account == 'Y':
                print("Please try your username again.")
                exit()
            elif no_account == 'N':
                print("Please create an account.")
                exit()
    login_password = input("Please enter your password: ")
    login_password1 = hashlib.md5(str.encode(login_password))
    login_password2 = login_password1.hexdigest()
    with open('passwords.txt') as e:
        if login_password2 in e.read():
            print("Login successful. Welcome to your personal home assistant, JIM.")
            main()

        elif login_password2 is not e.read():
            print("You got your password wrong you idiot.")


login()
