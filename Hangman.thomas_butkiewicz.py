"""
'''
_____________________________________________________________________________
|                                                                           |
|                                HANGMAN CODE                               |                                                    
|___________________________________________________________________________|    
|Thomas Butkiewicz                                                          |
|12/18/24                                                                   |                                                      
|Description: This runs a hangman Code with a random word chosen by my      |
|Dictionary. you have 6 chances to guess the word and if you do, you win,   |
|If not, you lose.                                                          |
|Bugs: It does not print the Body Hangman when you guess a word correctley. |
|The secret word I cut out because it was only printing the secret word but |
|after I removed it, it was using now all the worlds in the list.           |
|                                                                           |                                                                                                                                                                                                                               
|                                                                           |
|                                                                           |
|                                                                           |
|___________________________________________________________________________|

'''
"""
import random                                           #imports a random choice for word bank
print("Welcome to Hangman!!")                           #prints welcome to hangman
print('''+---+                                         
       |
       |
       |
      ===''')                                           #prints opening message shows the outline
hangman_pics = ['''         
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']                                               #hangman pics is the sign to print the hangman progression

words = ["american", "history", "python", "ramirahman", "lebronjames", "skibidy", "engineering", "inventory", "alleyoop", "cavaliers", "straffe"]       #This is the list of words that my hangman randomly chooses from
secret = random.choice(words)                                                                                                                           #This  is saying to choose a random word from the list
#secret = "sigma"
#print(secret)
secret_list=list(secret)                        #saying that the secret list is not supposed to pop up
hidden = []                                     #creates hidden counter
guesses = 0                                     #start the guesses at 0

for character in secret_list:                   # every word in secret list
    hidden.append("_ ")
print("".join(hidden))                          #print out the word

while guesses < len(hangman_pics)-1 and "_ " in hidden:     #while the guesses are matched with hangman pics
    while True:
        guess = str.lower(input("Enter any letter: "))      #print guess any letter

        if guess in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:    # list of all the letters avaible to enter for the hangman code
            break
    if guess in secret_list:                            #if the guess is in the secret list
        for index in range(len(secret_list)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print("".join(hidden))                          # if the letter is in print, print enter again
    else:   
        print("That letter is not in here!")            #if not print try again
        print("Try Again!") 
        guesses += 1                                    # add guess to guess count
        print(hangman_pics[guesses])                    # add a new image for hangman pics

if "_ " in hidden:
    print("You lost!")                                  # guesses more than 6
else:                                                   #print you lose
    print("You win!")                                   # if not and guess word
                                                        #print you win










