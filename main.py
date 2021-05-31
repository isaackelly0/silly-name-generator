"""Random Module"""
import random
"""Secondary Module"""
from secondary import decider
def main():
    """Load random silly name"""
    # Load a list of first names
    first = ("Jack", "Alex", "Barry", "Christine", 
    "Diane", "Elaine", "Frank", "Gary", "Heather", 
    "Isabella","Keith")
    #Load a list of middle names
    middle = ("'The Thunder'", "Edgelord", 
    "'The South will rise again!'", 
    "Punisher", "Fartmaster", "'Just the worst'")
    # Load a list of surnames
    last = ("Johnson", "Ajax", "Beauregard", 
    "Candi", "Dixon", "Ellis", "Frankfurt", 
    "Gregson", "Hews", "Kelly")

    while True:
    # choose a first name at random
    # assign first name to a variable
        first_name = random.choice(first)
        # determine if middle name is blank or not
        middle_name = decider(middle)
    # choose a surname at random
    # assign surname to a variable
        last_name = random.choice(last)
    # print the names to the screen in order in red font
        print("Hello my name is Isaac and this is my associate, ", end='')
        print("{}{}{}".format(first_name, middle_name, last_name))
    # ask the user to quit or play again
        try_again = input("\nTry again? Enter to continue, or n to exit:")
        if try_again.lower() == "n":
            break
if __name__ == "__main__":
    main()
