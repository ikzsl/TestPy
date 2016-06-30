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
        if count > 21:
            print("вы проиграли")
            break
        elif count == 21:
            print("вы набрали 21 !!!!")
            break
        else:
            print("У вас %d очков" %count)
    elif choice == "n":
        print("у вас %d очков и вы закончили игру" %count)
        break
print("досвидос")
