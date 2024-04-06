import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

print("\nWelcome to the game PIG!")

while True:
    players = input("Enter the number of players (2 - 4) ")
    if players.isdigit():
        players = int(players)
        if players < 2 or players > 4:
            print("\nPlease choose a number between 2 and 4.")
        else:
            break
        
    else:
        print('\nInvalid input. Please try again!')

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    
    for player_index in range(players):
        print(f"\nIt's player {player_index + 1}'s turn!")
        print(f"Score: {players_scores[player_index]}")
        current_score = 0
        
        while True:
            should_roll = input("\nWould you like to roll (y/n)?")
            if should_roll != 'y':
                break
            
            value = roll()
            if value == 1:
                print("Sorry you rolled a 1. Your turn is over.")
                current_score = 0
                break
            else:
                print(f"You rolled a: {value}")
                current_score += value
            
            print(f"Your score this turn is: {current_score}")
            
        players_scores[player_index] += current_score

top_score = max(players_scores)
winning_index = players_scores.index(max_score)
print("Player number ", winning_index + 1, " is the winner with a score of: ", max_score)
