import random

def secret_word(wordlist):
     return list( wordlist.pop( random.randint(1, len(wordlist)-1)))

def scramble_word(secret_word):
     shuffledWord = list(secret_word)
     random.shuffle(shuffledWord)
     return shuffledWord

def printWord(shuffledWord):
      print( "".join(shuffledWord).upper() )
# open the file 

def main():
     guessedword = []
     scrambledword = []
     guesses = 0
     letter = 0
     newletter = ""
     gameover = False
    # crate a list of words
     wordlist = []

     #fileName = input("enter the file name: ")
     #define the variable
     infile = open('wordlist.txt', 'r')

     # define a new variable for a line in the file
     line = infile.readline()
     wordlist.append(line)

     while (len(line) > 0):
          line = infile.readline()
          line = line.strip()
          wordlist.append(line)
          
     # close the file
     infile.close()

     print("Welcome to Crypto-Logic!\n"
           "Guess the word one letter at a time.\n")
     
     
     # select a word from the list
     word = secret_word(wordlist)
     

     # scramble the word
     scramble = scramble_word(word)
     

     while (not gameover):
          print("\nIncorrect guesses: " +str(guesses))

          printWord(scramble)
          printWord(guessedword)

          newletter = input("Guess a letter: ").lower()

          if ( word[letter] == newletter ):

               guessedword.append(newletter)
               letter += 1

          else:

               guesses += 1

          if ( len(guessedword) == len(word) ):

               gameover = True

     printWord(guessedword)

     print("\nCongratulations! You guessed the word in " + str(guesses) + " incorrect guesses!")

     input("Press ENTER to exit:")

     

main()
