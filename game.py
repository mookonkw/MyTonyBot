import random

from functions import (talk,
                       listen)


def play_game():
    my_score = 0
    tony_score = 0
    choices = ('rock', 'paper', 'scissors')
    talk(f'lets play a game of {choices}')
    print(f'lets play a game of {choices}')

    counter = 5

    while counter:
        talk(f'choose now')
        print(f'choose now')

        my_answer = listen().lower()
        print(my_answer)
        check = [True if x == my_answer else False for x in choices]
        if not any(check):
            print(f'your choice is invalid')
            talk(f'your choice is invalid, your choices are {choices}')
            continue
        talk(f'you chose {my_answer}')
        print(f'you chose {my_answer}')

        tony = random.choice(choices)

        counter -= 1
        talk(f'you chose {my_answer} and tony chose {tony}')
        print(f'you chose {my_answer} and tony chose {tony}')

        if my_answer == tony:
            my_score += 0.5
            tony_score += 0.5
            talk('its a tie, you have earned 0.5 points each')
            print('its a tie, you have earned 0.5 points each')

        elif my_answer == 'rock':
            if tony == 'paper':
                talk('tony wins, one point earned.')
                print('tony wins, one point earned.')
                tony_score += 1
            else:
                talk('you win, one point earned.')
                print('you win, one point earned.')
                my_score += 1
        elif my_answer == 'paper':
            if tony == 'scissors':
                talk('tony wins, one point earned.')
                print('tony wins, one point earned.')
                tony_score += 1
            else:

                talk('you win, one point earned.')
                print('you win, one point earned.')
                my_score += 1
        elif my_answer == 'scissors':
            if tony == 'rock':
                talk('tony wins, one point earned.')
                print('tony wins, one point earned.')
                tony_score += 1
            else:
                talk('you win, one point earned.')
                print('you win, one point earned.')
                my_score += 1

    else:
        if my_score > tony_score:
            talk(f'You won this round by {my_score} points')
            print(f'You won this round  by {my_score} points')
        elif my_score < tony_score:
            talk(f'Tony won this round by {tony_score} points')
            print(f'Tony won this round by {tony_score} points')
        else:
            talk(f'this round is a tie, you both earn {my_score} points')
            print(f'this round is a tie, you both earn {my_score} points')
