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

def keystream(deck, length):
    letter = ""
    while len(letter) < length:
        shuffle_deck(deck)
        move_joker_a(deck)
        move_joker_b(deck)
        split_deck(deck)
        move(deck)
        upper_card_value = deck[0]
        NOT_FALSE = True

        while NOT_FALSE:
            card_value = deck[(upper_card_value-1)]
            if card_value <= 26:
                letter += (chr(card_value + 64))
                NOT_FALSE = False
            else:break
    return letter

def kryptera(message, deck):
    conv_text = []
    conv_nyckelfras = []
    secret_message = ""
    message = message.upper()
    length = len(message)
    nyckelfras = keystream(deck, (len(message)))
    for i in message:
        conv_text.append((ord(i)-64))
    for i in nyckelfras:
        conv_nyckelfras.append((ord(i)-64))

    for i in range(length):
        res = 0
        x = conv_text[i]
        y = conv_nyckelfras[i]
        res = x + y
        if res > 26:
            res -= 26
        secret_message += (chr(res + 64))
    return secret_message
   
def dekryptera(message, deck):
    conv_message = []
    conv_nyckelfras = []
    dekrypt = ""
    nyckelfras = keystream(deck, (len(message)))
    for i in nyckelfras:
        conv_nyckelfras.append(ord(i)-64)
    for i in message:
        conv_message.append(ord(i)-64)
    for i in range(len(message)):
        res = 0
        x = conv_message[i]
        y = conv_nyckelfras[i]
        res = x - y
        if res < 1:
            res += 26
        dekrypt += (chr(res + 64))
    return dekrypt

deck1 = create_deck()
deck2 = create_deck()

secret = kryptera("Hejsan", deck1)
print("Krypterad nyckel: ",secret)
print("Dekrypterad: ",dekryptera(secret, deck2))