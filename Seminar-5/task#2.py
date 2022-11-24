# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random as r
move = r.getrandbits(1)


def bot_move(balance, step):
    return balance % (step + 1)


left = 121
max_take = 28
note = ' Next turn'
print(f'Initial conditions: Number of sweets: {left}, Max: {max_take}')

while left > 0:
    if move:
        bot_takes = bot_move(left, max_take)
        print(f' {left} sweets left. Computer takes: {bot_takes}')
        left -= bot_takes
        move = False
        if left == 0:
            print('Computer win!')
            break
        else:
            print(note)
    else:
        player2_take = int(input(f' {left} sweets left. Player takes: '))
        if player2_take not in range(1, max_take + 1):
            print(f' You have to take form 1 to  {max_take} sweets')
            continue
        left -= player2_take
        move = True
        if left == 0:
            print('You win!')
            break
        else:
            print(note)

print('Game over!')
