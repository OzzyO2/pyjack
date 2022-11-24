import tkinter as tk
from random import shuffle

class Card:

    def __init__(self, suit, colour, rank, value):
        """Initialise the attributes needed for a playing card"""
        self.suit = suit
        self.colour = colour
        self.rank = rank
        self.value = value

class Pyjack:

    def __init__(self):
        """Initialise values needed for the game to work"""
        self.suits = [
            "diamonds", "hearts", "spades", "clubs"
        ]
        self.colours = [
            "black", "red"
        ]
        self.ranks = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"
        ]
        self.deck = []

    def _create_deck(self):
        """Helper method to create a new, randomised deck"""
        for suit in self.suits: # Each suit contains 13 cards, with 52 unique cards in total
            if suit == "diamonds" or suit == "hearts":
                for rank in self.ranks:
                    if rank in self.ranks[:9]:
                        card = Card(suit, "red", rank, int(rank))
                        self.deck.append(card)
                    elif rank in self.ranks[9:12]:
                        card = Card(suit, "red", rank, 10)
                        self.deck.append(card)
                    else:
                        card = Card(suit, "red", rank, 11)
                        self.deck.append(card)

            if suit == "spades" or suit == "clubs":
                for rank in self.ranks:
                    if rank in self.ranks[:9]:
                        card = Card(suit, "black", rank, int(rank))
                        self.deck.append(card)
                    elif rank in self.ranks[9:12]:
                        card = Card(suit, "black", rank, 10)
                        self.deck.append(card)
                    else:
                        card = Card(suit, "black", rank, 11)
                        self.deck.append(card)
        shuffle(self.deck)
        print(len(self.deck))

    def _show_menu(self):
        """Helper method to show the starter, CLI menu"""
        self.option_chosen = False
        while not self.option_chosen:
            self.option = input("Would you like to play blackjack (Y/N): ")
            if self.option in ["Y", "y", "Yes", "yes"]:
                self.option_chosen = True
            else:
                print("Thank you for playing!")
                quit()

    def play(self):
        """Method containing the main loop for the game"""

        self._show_menu()
        self._create_deck()
 
if __name__ == "__main__":
    pyjack = Pyjack()
    pyjack.play()
