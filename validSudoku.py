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
        for m in range(0,9,3):
            for k in range(0,9,3):
                temprows=[]
                for i in range(m,3+m):
                    for j in range(k,3+k):
                        if(board[i][j].isnumeric()):
                            temprows.append(board[i][j])
                if len(temprows) != len(set(temprows)):
                    return False
                
        return True

def main():
    board =  [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    # board = [[".",".",".",".","5",".",".","1","."],
    #          [".","4",".","3",".",".",".",".","."],
    #          [".",".",".",".",".","3",".",".","1"],
    #          ["8",".",".",".",".",".",".","2","."],
    #          [".",".","2",".","7",".",".",".","."],
    #          [".","1","5",".",".",".",".",".","."],
    #          [".",".",".",".",".","2",".",".","."],
    #          [".","2",".","9",".",".",".",".","."],
    #          [".",".","4",".",".",".",".",".","."]]
    print(Solution().isValidSudoku(board))

if __name__ == "__main__":
    main()