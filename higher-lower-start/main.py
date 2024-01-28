#Import logo
import art
import game_data
import random
from replit import clear

# Pull data randomly from game_data and display for the user to make the choice.
# num_a = random.randint(0, len(game_data.data)-1)
# num_b = random.randint(0, len(game_data.data)-1)
score = 0
# print(game_data.data[num_a])
# print(game_data.data[num_b])
#printing A and B
def pull_data():
    num = random.randint(0, len(game_data.data)-1)
    name = game_data.data[num]['name']
    des = game_data.data[num]['description']
    country = game_data.data[num]['country']
    value = game_data.data[num]['follower_count']
    # print(game_data.data[num])
    return name, des , country, value
# Compare user choice and actual values
def compare(choice, val_a, val_b):
    if val_a > val_b:
        winner = "a"
        # print("a")
    elif val_a < val_b:
        winner = "b"
        # print("b")
    elif val_a == val_b:
        return True
    
    if winner == choice:
        return True
    else:
        return False
is_over = False

#pulling and replacing of a value depending on score
while not is_over:
    if score == 0:
        print(art.logo)
        name_a , des_a , country_a ,value_a = pull_data()
        print(f"Compare A:\t{name_a},a {des_a},from {country_a}")
        print(art.vs)
        name_b, des_b, country_b, value_b = pull_data()
        print(f"Against B:\t{name_b},a {des_b},from {country_b}")
        choice = str(input("Who has more followers? Type 'A' or 'B': ").lower())
        ans = compare(choice, value_a, value_b)
        if ans == True:
            score += 1
        else:
            print("Ooops You Guessed Wrong! You Lose!")
            is_over = True
    else:
        clear()
        print(art.logo)
        print(f"Your Score is {score}")
        # print(f"Compare A:\t{name_a},a {des_a},from {country_a}")
        name_a , des_a , country_a ,value_a =name_b, des_b, country_b, value_b
        print(f"Compare A:\t{name_a},a {des_a},from {country_a}")
        print(art.vs)
        while name_a  == name_b:
            name_b, des_b, country_b, value_b = pull_data()
        print(f"Against B:\t{name_b},a {des_b},from {country_b}")
        choice = str(input("Who has more followers? Type 'A' or 'B': ").lower())
        ans = compare(choice, value_a, value_b)
        if ans == True:
            score += 1
        else:
            print(f"Ooops You Guessed Wrong! You Lose! Your Final Score is {score}")
            is_over = True
        
        


# else:
#     name_a = name_b
#     des_a = des_b
#     country_a = country_b
#if correct increment user score and continue game by making b to a and new random data or b else if the player is wrong then display final score and end game
