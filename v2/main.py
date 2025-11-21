from game_data import data 
import random

game_on = True
score = 0

def random_numbers(data):
    random_number_1 = random.randint(0, len(data)-1)
    random_number_2 = random.randint(0, len(data)-1)
    if random_number_1 == random_number_2:
        random_number_2 = random.randint(0, len(data)-1)
    return random_number_1, random_number_2

def item_A(data, random_number_1):
    name_1 = data[random_number_1].get("name")
    followers_1 = data[random_number_1].get("follower_count")
    description_1 = data[random_number_1].get("description")
    country_1 = data[random_number_1].get("country")
    return name_1, followers_1, description_1, country_1

def item_B(data, random_number_2):
    name_2 = data[random_number_2].get("name")
    followers_2 = data[random_number_2].get("follower_count")
    description_2 = data[random_number_2].get("description")
    country_2 = data[random_number_2].get("country")
    return name_2, followers_2, description_2, country_2

def printing_AB(name_1, description_1, country_1, name_2, description_2, country_2):
    print(f"\nA: {name_1}, a {description_1}, from {country_1}")
    print(f"B: {name_2}, a {description_2}, from {country_2}")

def guessing():
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == "A" or guess == "B":
        return guess
    else:
        return guessing()

# ---------- GAME LOGIC ---------- #  
print("\n* * * * * HIGHER / LOWER GAME * * * * *")
while game_on:
    # ------------------------------------------------------------------
    random_number_1, random_number_2 = random_numbers(data)
    # ------------------------------------------------------------------
    name_1, followers_1, description_1, country_1 = item_A(data, random_number_1)
    name_2, followers_2, description_2, country_2 = item_B(data, random_number_2)
    # ------------------------------------------------------------------
    printing_AB(name_1, description_1, country_1, name_2, description_2, country_2)
    guess = guessing()
    print(guess)
    # ------------------------------------------------------------------
    if followers_1 > followers_2:
        result = "A"
    elif followers_1 < followers_2:
        result = "B"
    # ------------------------------------------------------------------
    if guess == result:
        score += 1
        print(f"\nYou're right! Current score: {score}")
    elif guess != result:
        print(f"\nYou're wrong! Final score: {score}")
        game_on = False
    