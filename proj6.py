#Name: Gloria Silva
#Assignment: proj6.py
#Date: Nov. 11, 2025
#Program Description: This program allows the user to play the game Rock, Paper, Scissors against the computer. It uses five functions, including the main function.  

ROCK = 0
PAPER = 1
SCISSORS = 2

import random

def introduction(): #This function prints the welcome message, gets the player's name and returns it, and prints out the game instructions.
    print('Welcome to the game Rock, Paper, Scissors. You will be playing against the computer.')
    players_name = input('What is your name?')
    print(f'Here are the rules {players_name}:')
    print('If a player chooses Rock and the other chooses Scissors, Rock wins.')
    print('If a player chooses Scissors and the other chooses Paper, Scissors wins.')
    print('If a player chooses Paper and the other chooses Rock, Paper wins.')
    print("If both players make the same choice, it's a tie.")
    print('Enter -1 to quit the game')
    return players_name
    
def get_user_play(): #This function gets the user's play selection from the keyboard and returns it.
    users_move = int(input('Enter your move (0 for Rock, 1 for Paper, 2 for Scissors):'))
    return users_move

def get_computer_play(): #This function uses a floating random number between 0 and 1 to get the computer's play and returns it.
    computers_move = random.random()
    if computers_move <0.25:
        computers_move = "Rock"
    elif computers_move >=0.25 and computers_move<=0.65:
        computers_move = "Paper"
    elif computers_move >0.25:
        computers_move = "Scissors"
    return computers_move

def print_statistics(num_games, player_wins, comp_wins, ties, players_name): #This function outputs the number of games played, and the total won by the player and the computer, as well as the number of ties. Receives arguments.
    print(f'There were {num_games} games: {players_name} won {player_wins} games, the computer won {comp_wins} games, and there were {ties} ties.')
    

def main(): #This function is the main function. It calls the introduction, get_user_play, get_computer_play, and print_statistics functions. 
    random.seed(451)
    players_name = introduction()
    print()
    num_games = 0
    player_wins = 0
    comp_wins = 0
    ties = 0
    SENTINEL = 0
    while SENTINEL != -1:
        users_move = get_user_play()
        computers_move = get_computer_play()
        num_games += 1
        if users_move == 0 and computers_move == "Scissors":
            print(f'{players_name} plays Rock and computer plays Scissors')
            print(f'Rock breaks scissors. {players_name} wins!')
            print()
            player_wins += 1
        elif users_move == 2 and computers_move == "Paper":
            print(f'{players_name} plays Scissors and computer plays Paper')
            print(f'Scissors cuts paper. {players_name} wins!')
            print()
            player_wins += 1
        elif users_move == 1 and computers_move == "Rock":
            print(f'{players_name} plays Paper and computer plays Rock')
            print(f'Paper covers rock. {players_name} wins!')
            print()
            player_wins += 1
        elif users_move == 2 and computers_move == "Rock":
            print(f'{players_name} plays Scissors and computer plays Rock')
            print('Rock breaks scissors. Computer wins!')
            print()
            comp_wins += 1
        elif users_move == 0 and computers_move == "Paper":
            print(f'{players_name} plays Rock and computer plays Paper')
            print('Paper covers rock. Computer wins!')
            print()
            comp_wins += 1
        elif users_move == 1 and computers_move == "Scissors":
            print(f'{players_name} plays Paper and computer plays Scissors')
            print('Scissors cuts paper. Computer wins!')
            print()
            comp_wins += 1
        elif users_move == -1:
            SENTINEL = -1 #This move ends the game.
        else:
            print(f'{players_name} plays {users_move} computer plays {computers_move}')
            print("It's a tie!")
            print()
            ties += 1
    num_games-=1
    print_statistics(num_games, player_wins, comp_wins, ties, players_name)
main()
        
        
        
        
            
        