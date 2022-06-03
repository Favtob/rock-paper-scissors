import random
import math

def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    user = user.upper()

    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return (0, user, computer)

    # R > S, S > P, p > R
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost \n'.format(user, computer))

    if player_wins > computer_wins:
        print('You have won ! You are undefeated'.format(n))
    else:
        print('Unfortunately, the computer has won. Work harder next time!'.format(n))


if __name__ == '__main__':
    play_best_of(1) # 2