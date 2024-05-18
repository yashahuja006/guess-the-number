import random
from time import sleep
def guess_the_number(n=1):
    print("DO YOU WANNA PLAY THE GAME ANSWER IN YES OR NO")
    D=input("yes or no:-")
    if D=="yes":
      print("get ready")

    else:
      print("bye")
      return 0

    a=int(input("guess a number  you have chosse from 1 to 6:-"))
    print("Dice Rolling...")
    sleep(3)
    b=random.randint(1,3)

    if a==b:
     print(f"you guessed correct in {n} attempts")
     return 0
    else:
     print("guessed wrong number")

     guess_the_number(n+1)

guess_the_number()






