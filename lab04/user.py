import ADT

def keystream(deck, length):
    letter = ""
    while len(letter) < length:
        ADT.shuffle_deck(deck)
        ADT.move_joker_a(deck)
        ADT.move_joker_b(deck)
        ADT.split_deck(deck)
        ADT.move(deck)
        card = ADT.create_pattern(deck) 
        letter += (chr(card + 64))
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

deck1 = ADT.create_deck()
deck2 = ADT.create_deck()

secret = kryptera("Hejsan", deck1)
print("Krypterad nyckel: ",secret)
print("Dekrypterad: ",dekryptera(secret, deck2))
