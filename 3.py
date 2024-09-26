import random


NUMBER_OF_GAME_STEPS = 5


def mini_rpg():
    player_health = 50
    opponent_health = 50

    for _ in range(NUMBER_OF_GAME_STEPS):
        print(f'\nYour health: {player_health}')
        print(f'Opponent health: {opponent_health}\n')

        number = int(input('Write 0 to attack or write 1 to health: '))

        while number != 0 and number != 1:
            number = int(
                input('Please, Write 0 to attack or write 1 to health: ')
            )

        if number == 0:
            opponent_health -= random.randint(5, 15)
        elif number == 1:
            player_health += random.randint(5, 10)

        player_health -= random.randint(5, 20)

        if player_health <= 0:
            print('\nYou lost!\n')
            return
        elif opponent_health <= 0:
            print('\nYou won!!!\n')
            return

    if player_health < opponent_health:
        print('\nYou lost!\n')
    elif player_health == opponent_health:
        print('\nDraw!\n')
    else:
        print('You won!!!')


mini_rpg()
