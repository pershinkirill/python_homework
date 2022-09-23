# Создайте программу для игры в ""Крестики-нолики"".


def player_input(player_symbol):
    valid = False
    while not valid:
        the_answer = input('where should be ' + player_symbol + ' placed? : ')
        try:
            the_answer = int(the_answer)
        except:
            print('error')
            continue
        if the_answer in range(1, 10):
            if str(board[the_answer-1]) not in 'XO':
                board[the_answer-1] = player_symbol
                valid = True
            else:
                print('greed is taken')
        else:
            print('please enter a number from 1 to 9')


def draw_board(state):
    print('_' * 13)
    for i in range(3):
        print('|', state[0 + i * 3], '|', state[1 + i * 3], '|', state[2 + i * 3], '|')
        print('-' * 13)


def victory(state):
    vic_chain = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for chain in vic_chain:
        if board[chain[0]] == state[chain[1]] == state[chain[2]]:
            return board[chain[0]]
    return False


def main(state):
    counter = 0
    finished = False
    while not finished:
        draw_board(state)
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        counter += 1
        if counter > 4:
            current = victory(state)
            if current:
                print(f'{current} WIN!!!')
                finished = True
                break
        if counter == 9:
            print('Draw')
            break
    draw_board(board)


board = list(range(1, 10))
main(board)
