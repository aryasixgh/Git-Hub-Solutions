class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int: 
        startRows = 0
        startCols = 0
        for s in range(1, min(len(matrix), len(matrix[0]))):
            submatrix = []
            for i in range(startRows, startRows+s):
                submatrixRow = []
                for j in range(startCols, startCols+s): 
                    submatrixRow.append(matrix[i][j])
                submatrix.append(submatrixRow)
                startCols += 1
            startRows += 1
        pass

def main():
    print(Solution().countSquares())

if __name__ == "__main__":
    main()