# Uppgift D

sum = 0

for n in range (2,1001):
    is_Prime = True
    for i in range(2,n):
        if n % i == 0:
            is_Prime = False
            break

    if is_Prime:
        sum += n
        print(sum)
