class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        listA = []
        listATwo = []
        listB = []
        listBTwo = []
        listC = []
        listCTwo = []
        for i in s:
            if i == '(':
                listA.append(i)
            elif i == ')':
                listATwo.append(i)
            elif i == '[':
                listB.append(i)
            elif i == ']':
                listBTwo.append(i)
            elif i == '{':
                listC.append(i)
            elif i == '}':
                listCTwo.append(i)
        
        if len(listA) != len(listATwo):
            return False
        if len(listB) != len(listBTwo):
            return False
        if len(listC) != len(listCTwo):
            return False
        
        return True

def main():
    print(Solution().isValid("([)]"))

if __name__ == "__main__":
    main()  