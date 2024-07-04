class SudokuSolver:

    def solver(self , board):
        if self.solve(board):
            return board
        
        return "Invalid Sequence Entered"
    
    def solve(self , board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1,10):
                        if self.isSafe(i , j , str(num) , board):
                            board[i][j] = str(num)
                            if self.solve(board[:]):
                                return 1
                            else:
                                board[i][j] = '.'
                    
                    return 0
        
        return 1
    
    def isSafe(self , row , col , num , board):
        for i in range(9):
            if board[row][i] == num:
                return 0
            
            if board[i][col] == num:
                return 0
            
            if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)] == num:
                return 0
        
        return 1

if __name__=="__main__":
    print("Enter the board details below\n")
    print("Note: Enter .(dot) for vacant spaces\n")
    board = ['']*9
    for i in range(9):
        print("Enter row", i+1)
        inp = list(map(str , input().split()))
        board[i] = inp

    object = SudokuSolver()
    print("The Solved Sudoku Looks Like:")
    solved = (object.solver(board))

    for i in range(9):
        for j in range(9):
            print(solved[i][j] , end = ' ')
        print()
