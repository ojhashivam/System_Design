class SudokuSolver:
    def solver(self , board):
        if self.solve(board):
            return True
        
        return False
    
    def solve(self , board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in range(1 , 10 , 1):
                        if self.isSafe(i , j , str(num) , board):
                            board[i][j] = str(num)
                            if self.solve(board):
                                return True
                            
                            board[i][j] = "."
                    
                    return False
        
        return True
                            
        
    
    def isSafe(self , row , col , num , board):
        for i in range(9):
            if board[row][i] == num:
                return False
            
            if board[i][col] == num:
                return False
            
            if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)] == num:
                return False
        
        return True

if __name__=="__main__":
    print("Enter the board details below\n")
    print("Note: Enter .(dot) for vacant spaces\n")
    board = []
    for i in range(9):
        print("Enter row", i+1)
        inp = list(map(str , input().split()))
        board.append(inp)

    print(board)
    object = SudokuSolver()
    solved = (object.solver(board))

    if solved:
        print("The Solved Sudoku Looks Like:")
        for i in range(9):
            for j in range(9):
                print(board[i][j] , end = ' ')
            print()
    
    else:
        print("Invalid Input")
