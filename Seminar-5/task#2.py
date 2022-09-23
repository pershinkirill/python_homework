# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random as r

def next_move(balance, step):
    return balance % (step + 1)


left = 542
max_take = 128
print(f'Initial conditions: Number of sweets: {left}, Max: {max_take}')

note = 'Your turn!'
my_move = r.getrandbits(1)

while left > 0:
    if my_move:
        print(f' {left} sweets left. I take {next_move(left, max_take)}.', end='')
        left = left - next_move(left, max_take)
        my_move = False

        if left == 0:
            note = message = 'I win!'
            print(note)
            break
        else:
            print(note)
    else:
        partner_take = int(input(f' {left} sweets left. Partner takes: '))
        if partner_take not in range(1, max_take+1):
            print(f' you have to take form 1 to  {max_take} sweets')
            continue
            # partner_take = int(input(f'осталось {left} конфет. Партнер берет конфет: '))
        else:
            left = left - partner_take
            my_move = True
            if left == 0:
                message = 'Partner won'
                break

print('Game over!')
