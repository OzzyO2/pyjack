import tkinter as tk
from random import shuffle

class Card:

    def __init__(self, suit, colour, rank):
        """Initialise the attributes needed for a playing card"""
        self.suit = suit
        self.colour = colour
        self.rank = rank

class Pyjack:

    def __init__(self):
        """Initialise values needed for the game to work"""
        self.suits = ["diamonds", "hearts", "spades", "clubs"]
        self.colours = ["black", "red"]
        self.ranks = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"
        ]
        self.deck = []

    def create_deck(self):
        """Method to create a new, randomised deck"""
        for suit in self.suits: # Each suit contains 13 cards, with 52 unique cards in total

            if suit == "diamonds" or suit == "hearts":
                for rank in self.ranks:
                    card = Card(suit, "red", rank)
                    self.deck.append(card)

            if suit == "spades" or suit == "clubs":
                for rank in self.ranks:
                    card = Card(suit, "black", rank)
                    self.deck.append(card)
        shuffle(self.deck)

    def play(self):
        """Method containing the main loop for the game"""
 
if __name__ == "__main__":
    pyjack = Pyjack()
    pyjack.play()
