import random

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def display_board(board):
    print(("+" + "-" * 7) * 3 + "+")
    for i in board:
        print(("|" + " " * 7) * 3 + "|")
        print(("|" + " " * 3 + i[0] + " " * 3) + ("|" + " " * 3 + i[1] + " " * 3) + (
                    "|" + " " * 3 + i[2] + " " * 3) + "|")
        print(("|" + " " * 7) * 3 + "|")
        print(("+" + "-" * 7) * 3 + "+")


def enter_move(board):
    list_move = make_list_of_free_fields(board)
    breaker = True
    while breaker:
        move_user = input("Enter your move: ")
        if int(move_user) in range(1, 10):
            for tup in list_move:
                if board[tup[0]][tup[1]] == move_user:
                    board[tup[0]][tup[1]] = "O"
                    breaker = False


def make_list_of_free_fields(board):
    list_of_free_fields = []
    for count, i in enumerate(board):
        for j, m in enumerate(i):
            if m != "X" and m != "O":
                tuple_row_column = (count, j)
                list_of_free_fields.append(tuple_row_column)
    return list_of_free_fields


def victory_for(board, sign):
    if sign == "X":
        name = "computer"
    else:
        name = "USER"
    if not make_list_of_free_fields(board):
        print("Draw in the game!!!")
        return True
    list_of_free_fields = []
    for count, i in enumerate(board):
        tuple_row_column = []
        for j, m in enumerate(i):
            if m == sign:
                tuple_row_column.append(j)
        list_of_free_fields.append(tuple_row_column)

    for k in list_of_free_fields:
        if len(k) == 3:
            print(name, "win!!!")
            return True
    if len(list_of_free_fields) == 3:
        for n in range(0, 3):
            if n in list_of_free_fields[0] and n in list_of_free_fields[1] and n in list_of_free_fields[2]:
                print(name, "win!!!")
                return True
        if 2 in list_of_free_fields[0] and 1 in list_of_free_fields[1] and 0 in list_of_free_fields[2]:
            print(name, "win!!!")
            return True
        if 0 in list_of_free_fields[0] and 1 in list_of_free_fields[1] and 2 in list_of_free_fields[2]:
            print(name, "win!!!")
            return True


def draw_move(board):
    list_move_comp = make_list_of_free_fields(board)
    move = random.choice(list_move_comp)
    board[move[0]][move[1]] = "X"


print("START GAME")
print()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print()
print("move computer: ")
board[1][1] = "X"
display_board(board)
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        display_board(board)
        break
    print("move computer: ")
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        display_board(board)
        break
print()
print("---------------------")
print("GAME OVER!!!")
