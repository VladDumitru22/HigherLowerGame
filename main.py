from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(value_A, value_B, guess):
    if value_A > value_B :
        return guess == 'A'
    else:
        return guess == 'B'

score = 0
game_should_continue = True
account_B = random.choice(data)

while game_should_continue:
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(f"Against B: {format_data(account_B)}")


    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    print("\n" * 20)

    value_A = account_A["follower_count"]
    value_B = account_B["follower_count"]

    is_correct = check_answer(value_A, value_B, guess)

    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}.")
    else:
        print(f"You lose! Final score: {score}.")
        game_should_continue = False