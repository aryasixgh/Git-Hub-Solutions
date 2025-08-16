class Solution:
    def maximum69Number (self, num: int) -> int:
        listNum = list(str(num))
        print(listNum)
        for i in range(len(listNum)):
            if listNum[i] == '6':
                listNum[i] = '9'
                break
        finalStr = ""
        for i in listNum:
            finalStr += i

        return finalStr
    
def main():
    print(Solution().maximum69Number(6999))

if __name__ == "__main__":
    main()