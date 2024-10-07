#Uppgift 2a

# DEL A
text = str(input("Ange din text: "))

def frame (text):
    i = 0
    while i < 2:
        n = -4 # n = -4 för att ge oss extar stjärnor så att den täcker hela texten
        while n < len(text): #while loop som är beronede på hur lång texten är
            print("*", end ="")
            n += 1 

        if i == 1: # om i är = 1 då har vi klarat det och ska breaka loopen
            print("")
            break
        else:
            print("\n*", text, "*") # printa ut texten
            i += 1

frame(text)

# DEL B
höjd = int(input("\nAnge Triangels höjd: "))

def triangle(höjd):
  for i in range(höjd):
      Rad = "*" * (2 * i + 1)
      print(Rad)
      
triangle(höjd)

#Del C
bredd = int(input("Ange Flaggans Bredd: "))

def flag(bredd):
    bredd = bredd * 20 // 2
    x = 0
   
    for n in range(16): #16 är höjden på flaggan
        if n == 8: #8 då är vi i miten av flagan så gör vi ett mellan rum 
            print("")
        for i in range(bredd):
            print("*", end="")
            
        print(" ", end= "")
        x += 1
        if x == 2:
            print("")
            x = 0

flag(bredd)

    
    

