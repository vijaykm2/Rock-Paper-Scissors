import random

user_choice = ''
choices = ['rock', 'paper', 'scissors']


def play_game():
    win_map = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    comp_choice = random.choice(choices)
    # print("computer choice = ", comp_choice)
    # Write your code here
    # print("user choice = ", user_choice)
    is_user_won = win_map.get(user_choice) == comp_choice;
    is_comp_won = win_map.get(comp_choice) == user_choice
    if is_user_won:
        print(f'Well done. The computer chose {comp_choice} and failed')
    elif is_comp_won:
        print(f'Sorry, but the computer chose {comp_choice}')
    else:
        print(f'There is a draw ({comp_choice})')

    play_or_exit()


def play_or_exit():
    global user_choice
    user_choice = input()
    invalid_input = True
    while invalid_input:
        if user_choice == '!exit':
            invalid_input = False
            print('Bye!')
            exit(0)
        elif user_choice in choices:
            invalid_input = False
            play_game()
        else:
            print("Invalid input")


play_or_exit()

