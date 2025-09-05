# Write your solution here
def play_turn(gb: list , x:int,y:int,piece:str):
    if y < 0 or y > 2:
        return False
    elif x < 0 or x > 2:
        return False
    elif piece == 'X' and gb[y][x] == 'O' or gb[y][x] == 'X':
        return False
    elif piece == 'X' and gb[y][x] == '':
        gb[y][x] = 'X'
        return True
    elif piece == 'O' and gb[y][x] == 'X' or gb[y][x] == "O":
        return False
    elif piece == 'O' and gb[y][x] == '':
        gb[y][x] = 'O'
        return True

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 0,0,"X"))
    print(game_board)
