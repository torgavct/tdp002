# Uppgift 1

namn = str(input("Vad heter du: "))
print ("Hej "+ namn)

ålder = int(input("Mata in din ålder: "))
print("Du föddes år ", (2024-ålder))

Län = str(input("Vilken län föddes du i: "))
print("Första halvan av ditt namn och andra halvan av ditt län är:", namn[:len(namn)//2] + Län[len(Län)//2:])
