#ADT
import random

def create_deck():
    deck = []
    for i in range(1, 29):
        deck.append(i)
    return deck
   
def shuffle_deck(deck):
    random.Random(3).shuffle(deck)
    return deck

def move_joker_a(deck):
    joker_position = get_joker_position(deck)
    if joker_position[0] == len(deck)-1:
        deck.insert(1, deck.pop(joker_position[0]))
    else:
        deck.insert((joker_position[0]-1), deck.pop(joker_position[0]))
        
def move_joker_b(deck):
    joker_position= get_joker_position(deck)
    if joker_position[1] == len(deck)-1:
        deck.insert(2, deck.pop(joker_position[1]))
    elif joker_position[1] == len(deck)-2:
        deck.insert(1, deck.pop(joker_position[1]))
    else:
        deck.insert((joker_position[1]-2), deck.pop(joker_position[1]))

def get_joker_position(deck):
    joker_dic = {"a" : 0, "b" : 0}
    joker_dic["a"] = deck.index(27)
    joker_dic["b"] = deck.index(28)
    joker_a = joker_dic.get("a")
    joker_b = joker_dic.get("b")
    joker_position = [joker_a, joker_b]
    return joker_position

def split_deck(deck):
    joker_position = get_joker_position(deck)
    if joker_position[0] > joker_position[1]:
        part_a = deck[:joker_position[1]]
        part_b = deck[joker_position[1]:(joker_position[0]+1)]
        part_c = deck[(joker_position[0]+1):]
    else:
        part_a = deck[:joker_position[0]]
        part_b = deck[joker_position[0]:(joker_position[1]+1)]
        part_c = deck[(joker_position[1]+1):]
    new_deck = part_c + part_b + part_a
    return new_deck

def move(deck):
    last_card_value = deck[len(deck)-1]
    moving_cards = deck[:last_card_value]
    deck[27:27] = moving_cards
    for i in range(len(moving_cards)):
        deck.pop(0)

