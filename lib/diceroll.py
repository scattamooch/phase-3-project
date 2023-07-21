import sys
from random import randint
import time

def generate_dice_roll(desired_sum, reset=True):
    global dice_result

    if reset or dice_result is None:
        dice_result = None
        while dice_result is None or sum(dice_result) <= desired_sum:
            dice_result = [randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)]
            sys.stdout.write("Generating dice rolls: ")
            sys.stdout.write(" ".join(str(num) for num in dice_result))  # Print the current diceroll values
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\r")
        sys.stdout.write("\n")
        return dice_result
    else:
        return reset == True
# desired_sum = 72
# dice_result = generate_dice_roll(desired_sum)

#print("Desired sum of 72 achieved!")
# print("Final Dice Roll:", dice_result)