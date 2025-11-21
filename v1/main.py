from art import logo
from art import vs
from game_data import data
import random

# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# GLOBAL VARIABLES
SCORE = 0
GAME = True

# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# FUNCTIONS
def printing_logo(logo):
    print(logo)

def random_number_generator():
    '''This function generates random numbers for "A" and "B". '''
    number_a = random.randint(0,49)
    number_b = random.randint(0,49)

    if number_a != number_b:
        return number_a, number_b
    else:
        random_number_generator()

def printing_a_b():
    '''This function prints the data of "A" and "B".'''

    data_a = data[number_a]
    data_b = data[number_b]

    print(f"\nCompare A: \nname:           {data_a["name"]}, \ndescription:    {data_a["description"]}, \ncountry:        {data_a["country"]}")
    print(f"\n{vs}")
    print(f"\nCompare B: \nname:           {data_b["name"]}, \ndescription:    {data_b["description"]}, \ncountry:        {data_b["country"]}")

    return data_a, data_b

def followers(data_a, data_b):
    '''This function collects the number of followers of "A" and "B".'''
    follower_number_a = int(data_a["follower_count"])
    follower_number_b = int(data_b["follower_count"])

    #print(f"\n{follower_number_a}")
    #print(follower_number_b)

    if follower_number_a > follower_number_b:
        higher_score = "a"
        #print(f"higher score: {higher_score}")
        return higher_score
    else:
        higher_score = "b"
        #print(f"higher score: {higher_score}")
        return higher_score


def betting():
    '''This function let the player choose from "A" and "B" and collects the answer.'''
    answer = input("\nWho has more followers? Type 'A' or 'B': \n").lower()

    if answer == "a" or answer == "b":
        print(f"answer: {answer}")
        return answer
    else:
        pass

def comparing(fact, bet):
    '''This function checks whether player's answer is the same as the comparison.'''
    global SCORE
    global GAME
    if fact == bet:
        SCORE = SCORE + 1
        print("\n" * 20)
        print(f"\nYour answer's right. Current score: {SCORE}")
        return SCORE
    else:
        print(f"\nYour answer's wrong. Final score: {SCORE}")
        GAME = False
        return GAME


# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# PROGRAM STRUCTURE

while GAME:
    printing_logo(logo)
    number_a, number_b = random_number_generator()
    data_a, data_b = printing_a_b()
    higher_score = followers(data_a, data_b)
    players_answer = betting()
    GAME = comparing(higher_score, players_answer)




