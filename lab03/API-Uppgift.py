#API
import requests

def request(url): #Hämta all data
    response = requests.get(url)
    if response.status_code == 200: #Om urlen är korrekt så sker detta.
        data = response.json()
        return data
    else:
        main() #Om det failar så kör vi om.

def find_pokemon(poke_name, data, url):
    for poke_index in range(data["count"]): #poke_index kommer bli ett nummer och då använda som en index indicator som kommer att gå igenom varje pokemon namn. Utifrån count: värdet som är det totala längden av dict.
        name = data["results"][poke_index]["name"] #Så vi går in i dict och tar värdet av results som är en lista, och utifrån listan så kommer vi in till en annan dic och d tar vi värdet på namn och checkar om det matchar anvädnarens input.
        if name == poke_name:
            return poke_index
        
def get_ability(poke_name, poke_index, url):
    poke_index += 1 #Poke-index +1 för att indexet kommer representerar inte dens /x/ format.
    url += "/"+str(poke_index)+"/"# Vi skapar den nya url:en med pokemonens index(plats)
    ability_data = request(url)# Anroper samma funktion och får fram den nya sidan av url:en.
    i = 0
    print("\n"+poke_name, "has",len(ability_data["abilities"]), "abilities.") # Printar ut namnet och dessutom antalet abilities den har.
    
    while i < len(ability_data["abilities"]): 
        move = ability_data["abilities"][i]["ability"]["name"]
        print("\nAbility '"+move+"':")
        
        new_url = ability_data["abilities"][i]["ability"]["url"]
        original_url = url[38:]
        url = url.replace(original_url, new_url)
        
        ability_text(url)
        i += 1
    print("")

def ability_text(url):
    
    effect_dic = request(url)
    ability_desc = effect_dic["effect_entries"][0]["short_effect"]
    print(ability_desc)
        
            
def main():
    url = "https://www.ida.liu.se/~TDP002/pokeapi/api/v2/pokemon" #Skapar en variable som innehåller url:en
    data = request(url) #Vi requestar om det är möjligt att koppla till url:en och dessutom få innehålllet av url:en.
    while True: # While true som kommer hålla hos inom huvud menyn och går aldrig ut.
        try:#Try catch så om man skriver ngt som inte matchar en pokemon så kommer en fel meddelande och kör om frågan.
            poke_name = str(input("Enter a Pokémon name: "))
            poke_index = find_pokemon(poke_name, data, url) #Kör hitta pokemon namn funktionen och dessutom skickar in parameter, namnet användaren skrev, dictonaryn från url, och själva url:en
            get_ability(poke_name, poke_index, url)
        except:
            print("\nPlease Try Again!\n")

if __name__ == "__main__":
    main()
  
