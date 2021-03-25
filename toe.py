import random

# create a counter that adds to self.col

class toe:
    marker = '|'
    def possibilities(self, board): 
        arr = board
        l = [] 
      
        for i in range(len(arr)): 
            for j in range(len(arr[0])): 
              
                if arr[i][j] == '-': 
                    l.append((i, j)) 
        return l
    
    def computerPicks(self, choices, board):
        location = random.choice(choices)
        if board[location[0]][location[1]] == '0' or board[location[0]][location[1]] == 'X':
            print('Comp: spot already taken, turn skipped')
        else:
            board[location[0]][location[1]] = 'X'
        return board
    
    def userPicks(self, board):
        user_row = int(input('Pick a row: '))
        user_col = int(input('Pick a column: '))
        if user_col % 2 != 0:
            raise ValueError('cant pick odd numbers')
        if (user_row < 0 or user_row > len(board) - 1) or (user_col < 0 or user_col > len(board[0]) - 1):
            print('not even on the board. turn skipped')
        elif board[user_row][user_col] == 'X' or board[user_row][user_col] == '0':
            print('User: spot already taken, turn skipped')
        else:
            board[user_row][user_col] = '0'
        return board

    def winnerH(self, board, row):
        for i in range(len(board)):
            if board[i].count('X') == row:
                return 'X wins'
            elif board[i].count('0') == row:
                return '0 wins'
            elif board[i].count('X') == row and board[i].count('X') == row:
                return 'It is a draw'

    def winnerV(self, board, row):
        transpose = list(zip(*board))
        for i in range(len(transpose)):
            if transpose[i].count('X') == row:
                return 'X wins'
            elif transpose[i].count('0') == row:
                return '0 wins'
            elif transpose[i].count('X') == row and transpose[i].count('X') == row:
                return 'It is a draw'

    def winnerD(self, board, row):
        back = []
        for x, y in enumerate(reversed(range(len(board)))):
            back.append(board[x][y*2])
        front = list(board[i][i*2] for i in range(len(board)))
        if front.count('X') == row:
            return 'X wins'
        elif front.count('0') == row:
            return '0 wins'
        if back.count('X') == row:
            return 'X wins'
        elif back.count('0') == row:
            return '0 wins'
        

    def print_board(self, board):
        for i in board:
            print(''.join(i))







def main():
    row = int(input('number of rows: '))
    col = int(input('number of columns: '))
    def create_board(row, col):
        marker = '|'
        d = col + 2
        final = []
        board = ['-' * d for i in range(row)]
        for i in board:
            for j in enumerate(i):
                excel = list(j)
                if excel[0] % 2 != 0:
                    excel[1] = marker
                final.append(excel[1])
        arr2 = [final[l:l+d] for l in range(0, len(final), d)]
        return arr2

    new_toe = toe()
    counter = 0
    board = create_board(row, col)
    for i in range(10000):
        choices = new_toe.possibilities(board)
        if len(choices) == 0:
            print('it is a draw!')
            break
        print('Choices are here: ', choices)
        user_pick = new_toe.userPicks(board)
        new_toe.print_board(user_pick)
        pick = new_toe.computerPicks(choices, board)
        new_toe.print_board(pick)
        if new_toe.winnerH(pick, row):
            print(new_toe.winnerH(pick, row))
            break
        if new_toe.winnerV(pick, row):
            print(new_toe.winnerV(pick, row))
            break
        if new_toe.winnerD(pick, row):
            print(new_toe.winnerD(pick, row))
            break
        counter += 1
        print('turn count: ' + str(counter))

if __name__ == '__main__':
    print('Ex: 4x4 is 4 rows and 5 columns', end='\n')
    print('Ex: 5x5 is 5 rows and 7 columns. 6x6 is 6 rows 9 columns')
    main()