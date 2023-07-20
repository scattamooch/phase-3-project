import sys
from random import randint
import time

def generate_dice_roll(desired_sum):
    diceroll = None
    while diceroll is None or sum(diceroll) <= desired_sum:
        diceroll = [randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)]
        sys.stdout.write("Generating dice rolls: ")
        sys.stdout.write(" ".join(str(num) for num in diceroll))  # Print the current diceroll values
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r")
    sys.stdout.write("\n")
    return diceroll

desired_sum = 72
diceroll = generate_dice_roll(desired_sum)

#print("Desired sum of 72 achieved!")
print("Final Dice Roll:", diceroll)