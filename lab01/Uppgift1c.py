# Uppgift 1c
n = 1
i = 1
j = 1
state = True

while n < 14:
    for j  in range (1, 14):
       res =  i % j # Vi ska använda modulo på i med alla tal mellan 1-13 (j)  

       if res == 0: #Om j får plats i i så betyder det att i har en  MÖJLIGhet att bli det talet, men vi behhåller i men ändrar på j + 1 för att kolla om nästa nummer kan få plats i i
           state = True
           print(i)
           
          
       else: # Om det är så att j får inte plats i i så stämmer inte j o vi måste ändra j med +1 o checka nya nummret.
           state = False
           i +=1
       
        
        
