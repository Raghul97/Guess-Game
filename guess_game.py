from random import randint
from sys import argv


def choose(initial, final):
    crct_val = randint(initial, final)
    return crct_val


def guess(initial, final):
    while True:
        try:
            guess_val = int(input(f'Guess the number between {initial} and {final}: '))
        except ValueError as err:
            print(err)
            print('This is a guess game between specified numbers, So only numbers are accepted.')
        else:
            if initial <= guess_val <= final:
                return guess_val
            print(f'Kindly enter the value between {initial} and {final}')


def check(initial, final, crct_val):
    chance = 5
    while True and chance != 0:
        choosen = guess(initial, final)
        if choosen > crct_val:
            print('oops, too high!!')
            chance -= 1
        elif choosen < crct_val:
            print('oops, too low!!')
            chance -= 1
        else:
            break
    if chance == 0:
        print('Sorry!, you have run out of chances.')
    else:
        print('Congrats!! you have guessed the number correctly.')


def play_again():
    player_choice = input('Do you want to play again? (y/n)  ')
    if player_choice[0].lower() == 'y':
        return True
    print('Thanks for Playing :) ')
    return False


if __name__ == '__main__':
    initial = 0
    final = 0
    try:
        initial = int(argv[1])
        final = int(argv[2])
    except ValueError:
        print('Arguments passed are not valid numbers, So default values are choosen.')
    except IndexError:
        print('No arguments have passed, So default values are choosen.')
    initial = 1 if not initial else initial
    final = 10 if not final else final
    game = True
    while game:
        value = choose(initial, final)
        check(initial, final, value)
        game = play_again()
