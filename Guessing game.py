from random import randint
from time import sleep

victory = False
count_defeats = 0
while not victory:
    num_drawn = randint(0, 9)
    print("-=-" * 20)
    print("I'll think of a number from 0 to 9. Try to guess ...")
    print("-=-" * 20)
    sleep(1)
    num = int(input("So, what number did I think? "))
    print("PROCESSING...")
    sleep(3)
    if num == num_drawn:
        print("Congratulations, you got it right!")
        victory = True
    else:
        print("You got it wrong, the number was: ", num_drawn)
        count_defeats += 1
print(f"You got it right on the {count_defeats + 1}º attempt!")