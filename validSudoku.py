class Solution:
    def isValidSudoku(self, board: list[list[str]]):
        #Check rows
        #Check cols
        for i in range(0, len(board)):
            tempRowArray = []
            tempColArray = []
            for j in range(0, len(board)):
                if(board[i][j].isnumeric()):
                    tempRowArray.append(board[i][j])
                if(board[j][i].isnumeric()):
                    tempColArray.append(board[j][i])
                if len(tempRowArray) != len(set(tempRowArray)) or len(tempColArray) != len(set(tempColArray)):
                    return False

        #Check 3x3
        return True

def main():
    board =  [["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))

if __name__ == "__main__":
    main()