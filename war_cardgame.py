import random
import pdb

####### --- GLOBAL VARS --- #######
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

####### --- CLASSES --- #######
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_card(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.' 


####### --- GAME LOGIC --- #######

# Set up players and deck
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()

# Shuffle the deck and deal cards to each player
new_deck.shuffle()
len(new_deck.all_cards)/2

for x in range(26):
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

# Start the game loop
game_on = True

# Initialize round number
round_num = 0

while game_on:
    # Increment round number
    round_num += 1
    print(f"Round {round_num}")
    
    # Check if either player is out of cards
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Start a new round and prepare for card comparison
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_card())
    
    at_war = True

    while at_war:
        # Compare the values of the last card in each player's current cards
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Player One wins the round
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False  # End the war
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # Player Two wins the round
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False  # End the war
        else:
            print('WAR!')
            # Both players' cards have equal values, initiate a war
            # Check if both players have enough cards to continue the war
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
            else:
                # Add additional cards to each player's current cards for the war
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
