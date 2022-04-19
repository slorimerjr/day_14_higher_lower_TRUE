import random
from art import logo
from art import vs
from game_data import data


# pull 2 random items from the imported list
def randomize_choice():
    return random.choice(data)

def find_answer(choice_a, choice_b):
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"

def map_choices(choice_a, choice_b):
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")


print(logo)
def game(): 
    score = 0
    keep_playing = True
    while keep_playing == True:
        choice_a = randomize_choice()
        choice_b = randomize_choice()
        map_choices(choice_a, choice_b)
        answer = find_answer(choice_a, choice_b)
        print(f"Psst! The answer is {answer}!")
        guess = input("Who has more follower? A or B: ").lower()
        if guess == answer:
            score += 1
            print(f"You're right! Currenct score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            keep_playing = False
game()