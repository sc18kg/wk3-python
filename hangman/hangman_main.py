
import random
from hangmanwords import word_list
from string import ascii_lowercase
from os import system
from sys import platform

life = 8

def select_random_word():
        return random.choice(word_list).lower()

if platform.startswith("linux"):
    clear_cmd = "clear"
elif platform.startswith("win"):
    clear_cmd = "cls"
elif platform.startswith("darwin"):
    clear_cmd = "clear && printf '\e[3J'"

clear = lambda : system(clear_cmd)

def hangman(life, tried_letters):
    print ("""
            [*]Hangman[*]
   
          """)
    print ("LIFE: {0}".format(life))
    if len(tried_letters) >= 1:
        print("Used letters: {}".format(", ".join(letters for letters in tried_letters)))

    if life == 6:
        print (" _________     ")
        print ("|         |    ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")

    elif life == 5:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")

    elif life == 4:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|         |    ")
        print ("|              ")
        print ("|              ")
        print ("|              ")

    elif life == 3:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|        /|    ")
        print ("|              ")
        print ("|              ")
        print ("|              ")

    elif life == 2:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|        /|\\  ")
        print ("|              ")
        print ("|              ")
        print ("|              ")

    elif life == 1:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|        /|\\  ")
        print ("|        /     ")
        print ("|              ")
        print ("|              ")

    elif life == 0:    
        print (" _________     ")
        print ("|         |    ")
        print ("|         0    ")
        print ("|        /|\\  ")
        print ("|        / \\  ")
        print ("|              ")
        print ("|              ")
    print("\n\n")

def print_error(why):
    print(why)

def play_again():
    prompt = str(input("\n\nWanna play again? ")).lower()
    yes = ['yes','y', 'ye', 's','sim','si']
    no = ['no', 'n', 'nao', 'na']
    if prompt in yes:
        global life
        life = 8
        main()
    elif prompt in no:
        print ("\nOkay then...")
        exit(0)
    else:
        print("\nWell I guess this is a yes.. ?")
        input()
        main()

def play(letters, random_word, life):
    #print (random_word) #the answer, for debugging
    tried_letters = []

    while True:
        try:
            hangman(life, tried_letters)

            for letter in letters:
                print(letter, end=' ')
            letter_input = str(input("Letter: ")).lower()

            if len(letter_input) > 1 or letter_input not in ascii_lowercase:
                print_error("Invalid Input\nOnly single letters")
                continue
            if letter_input in tried_letters:
                print_error("You already tried this letter!")
                continue 
    
            else:
                tried_letters.append(letter_input)
                if letter_input in random_word:
                    
                    letter_index = [index for index, value in enumerate(random_word) if value == letter_input]
                    
                    if len(letter_index) > 1:
                        for i in letter_index:
                            letters[i] = letter_input
                    elif letter_input in letters:
                        print_error("You already tried this letter!")
                        continue
                    else:
                        letters[letter_index[0]] = letter_input
                else:
                    life -= 1
                
                if ''.join(letters) == random_word:
                    hangman(life, tried_letters)                
                    for letter in letters:
                        print(letter, end=' ')                
                    print('\nThe word is {0}. You win!'.format(random_word))
                    input()
                    play_again()

                elif life == 0:
                    hangman(life, tried_letters)
                    print('\nThe word is {0}'.format(random_word))
                    print("The Hangman was hanged. You loose!")
                    input()
                    play_again()

        except IndexError:
            print_error("Invalid Input\nOnly single Letters") 
            continue

def main():
    try:
        while True:
            
            random_word =select_random_word()
            letter_list = list(random_word)
            word_length = len(random_word)
            letters = []
        
            for index in range(word_length):
                letters.append("_")
            play(letters, random_word, life)
    except KeyboardInterrupt:
        print("\n\nUser Requested Interruption!\nBye!")
        exit(0)
    
if __name__ == '__main__':
    main()