# Scrabble
# Word passed in can be made from tiles
# Initialise it with a string of 7 random letters
# Method to return score for submitted word
# Method for user input ?
# method that used the above to check a word is valid
# if it is , return score for word
# 

from random import shuffle

letter_value = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
"g": 2, "h": 4, "i": 1, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}

class Scrabble():

    def word_submit(self, word):
        self.word = word

    def return_score(word):
        return sum(letter_value[letter] for letter in word)
    
    def check_valid(self, word):
        pass

class Tile:

    def __init__(self, letter, letter_val):
        self.letter = letter.lower()
        if self.letter in letter_val:
            self.score = letter_val[self.letter]
        else:
            self.score = 0

class Deck():
    def __init__(self):
        self.deck = []
        self.init_deck()

    def add_to_deck(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)

    def init_deck(self):
        global letter_value
        self.add_to_deck(Tile("a", letter_value), 9)       
        self.add_to_deck(Tile("b", letter_value), 2)       
        self.add_to_deck(Tile("c", letter_value), 2)       
        self.add_to_deck(Tile("d", letter_value), 4)       
        self.add_to_deck(Tile("e", letter_value), 12)       
        self.add_to_deck(Tile("f", letter_value), 2)       
        self.add_to_deck(Tile("g", letter_value), 3)       
        self.add_to_deck(Tile("h", letter_value), 2)       
        self.add_to_deck(Tile("i", letter_value), 9)       
        self.add_to_deck(Tile("j", letter_value), 9)       
        self.add_to_deck(Tile("k", letter_value), 1)       
        self.add_to_deck(Tile("l", letter_value), 4)       
        self.add_to_deck(Tile("m", letter_value), 2)       
        self.add_to_deck(Tile("n", letter_value), 6)       
        self.add_to_deck(Tile("o", letter_value), 8)       
        self.add_to_deck(Tile("p", letter_value), 2)       
        self.add_to_deck(Tile("q", letter_value), 1)       
        self.add_to_deck(Tile("r", letter_value), 6)       
        self.add_to_deck(Tile("s", letter_value), 4)       
        self.add_to_deck(Tile("t", letter_value), 6)       
        self.add_to_deck(Tile("u", letter_value), 4)       
        self.add_to_deck(Tile("v", letter_value), 2)       
        self.add_to_deck(Tile("w", letter_value), 2)       
        self.add_to_deck(Tile("x", letter_value), 1)       
        self.add_to_deck(Tile("y", letter_value), 2)       
        self.add_to_deck(Tile("z", letter_value), 1)       
        self.add_to_deck(Tile("#", letter_value), 2)       
        shuffle(self.deck)

    def take_from_deck(self):
        return self.deck.pop()

class Hand:
    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        self.initialize()

    def add_to_hand(self):
        self.hand.append(self.deck.take_from_deck())

    def get_hand_str(self):
        return ", ".join(str(item.get_letter()) for item in self.hand)
    
    def get_hand_arr(self):
        return self.hand

    def initialize(self):
        for i in range(7):
            self.add_to_hand

class Player:

    def __init__(self, deck):
        self.hand = Deck(deck)
        self.score = 0

    def get_hand_str(self):
        return self.hand.get_hand_str()

    def get_hand_arr(self):
        return self.hand.get_hand_arr()

    def inc_score(self, inc):
        self.score += inc

    def get_score(self):
        return self.score