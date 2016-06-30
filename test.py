koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)

count = 0
while True:
    choice = input("Будете брать карту? y/n\n")
    if choice == "y":
        current = koloda.pop()
        print("карта %d" %current)
        count += current


        
        print(count)
