from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

account_A = random.choice(data)
account_B = random.choice(data)
if account_A == account_B:
    account_B = random.choice(data)

print(f"Compare A: {format_data(account_A)}")
print(f"Against B: {format_data(account_B)}")


#Ask user for a guess

#Get follower value of each account

#Check if the user is correct

#Get feedback to user

#Score tracking

#Make the game repeatable

#Make the account at position B to become the next account at position A

