"""Random Module"""
import random
def decider(names):
    """Returns a random choice from tuple or empty string"""
    decide = random.randrange(1,4)
    if decide == 3:
        return " "+random.choice(names)+" "
    return " "