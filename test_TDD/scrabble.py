# Scrabble
# Word passed in can be made from tiles
# Initialise it with a string of 7 random letters
# Method to return score for submitted word
# Method for user input ?
# method that used the above to check a word is valid
# if it is , return score for word
# 
import random

letter_value = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
"g": 2, "h": 4, "i": 1, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}

tile = "abcdefghijklmnopqrstuvwxyz"

class Game:
    def __init__(self):
        self.total_score = 0
    
    def single_round(self):
        self.hand = ScrabbleHand()
        print(self.hand.get_hand)
        self.guess = self.get_word_guess()
        score = self.hand.calc_score(self.guess)
        self.total_score += score


    def get_word_guess(self):
        guess = input(f"Please Enter The Guess Using the Words : {self.hand}")

    def main(self):
        while True:
            self.single_round()
            new_round = self.play_again()
            if not new_round:
                break
            print(self.exit_message())


class ScrabbleHand:
    def __init__(self):
        self.hand = ""
        for i in range(7):
            self.hand += (random.choice(tile))

    def get_hand(self):
        return self.hand
    
    def is_valid_word(self, word_check):
        for char in word_check:
            if char not in self.hand:
                return False
        else:
            self.hand[char] -= 1
            if self.hand[char] < 0:
                return False
        return True

    def calc_score(self, word):
        word_score = 0
        for x in word:
            word_score += letter_value[x]
        return word_score

g = Game()
sh = ScrabbleHand()

print(sh.get_hand())