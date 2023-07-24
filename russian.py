import random
import time
def game():
    x = 1 #Enemy
    y = 1 #Player
    gamemaker= random.randint(1,6)
    while (x != gamemaker) or (y != gamemaker):
        print("Enemy's turn!")
        x += 1
        time.sleep(5)
        print("Your turn!")
        y += 1
    if (x !=gamemaker) and (y == gamemaker):
        print("You have won the match!")
    else:
        print("Your enemy has won the match!")

game()
