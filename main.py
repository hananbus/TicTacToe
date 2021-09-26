import random

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
players = ['player 1', 'player 2']
markers = ['X', 'Y']
result = [0, 0]
available_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} \n"
          "---+---+---\n"
          f" {board[3]} | {board[4]} | {board[5]}\n"
          "---+---+---\n"
          f" {board[6]} | {board[7]} | {board[8]}\n")


def change_names():
    global players
    players[0] = input("Enter player 1 name: ")
    players[1] = input("Enter player 2 name: ")


def check_winners(player):
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] and board[i] == board[i + 2]:
            result[player] += 1
            print(f"{players[player]} is the winner !")
            return True
    for i in range(0, 3):
        if board[i] == board[i + 3] and board[i] == board[i + 6]:
            result[player] += 1
            print(f"{players[player]} is the winner !")
            return True
    if board[0] == board[4] and board[0] == board[8]:
        result[player] += 1
        print(f"{players[player]} is the winner !")
        return True
    if board[2] == board[4] and board[2] == board[6]:
        result[player] += 1
        print(f"{players[player]} is the winner !")
        return True
    else:
        return False


def game_play():
    display_board()
    start_player = random.randint(0, 1)
    second_player = (start_player + 1) % 2
    print(f"{players[start_player]} is starting")
    # check if there is still legal plays
    while True:
        wrong_input = True
        if len(available_numbers) == 0:
            return False
        while wrong_input:
            start_player_play = int(input(f"{players[start_player]} select you're play: "))
            if start_player_play in available_numbers:
                board[start_player_play] = markers[start_player]
                available_numbers.remove(start_player_play)
                wrong_input = False
                display_board()
                # game over
                if check_winners(start_player):
                    return True
            else:
                print("illegal play, try again!")
        wrong_input = True
        # check if there is still legal plays
        if len(available_numbers) == 0:
            return False
        while wrong_input:
            second_player_play = int(input(f"{players[second_player]} select you're play: "))
            if second_player_play in available_numbers:
                board[second_player_play] = markers[second_player]
                available_numbers.remove(second_player_play)
                wrong_input = False
                display_board()
                # game over
                if check_winners(second_player):
                    return True
            else:
                print("illegal play, try again!")


def starting_game():
    # select names
    print("Welcome to Tic Tac Toe game !!\n")
    if input("Do you want to enter names? if yes print 'Y': ").upper() == 'Y':
        change_names()


def select_markers():
    global markers
    wrong_input = True
    while wrong_input:
        player1 = input(f"What marker {players[0]} want to be? X or O: ").upper()
        if player1 == 'X':
            print(f"{players[0]} is X and {players[1]} is O")
            markers = ['X', 'O']
            wrong_input = False
        elif player1 == 'O':
            print(f"{players[0]} is O and {players[1]} is X")
            markers = ['O', 'X']
            wrong_input = False
        else:
            print("the option is X or O, please try again.")


starting_game()
select_markers()
if game_play():
    print(f"The result now is:\n {players[0]} : {result[0]}\n {players[1]} : {result[1]}")
else:
    print("a tie !!")

play_again = True
while play_again:
    if input("Do you want to play again? if yes type 'Y': ").upper() != 'Y':
        play_again = False
    else:
        board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        available_numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        select_markers()
        if game_play():
            print(f"The result now is:\n {players[0]} : {result[0]}\n {players[1]} : {result[1]}")
        else:
            print("a tie !!")

print("thanks for playing !")
