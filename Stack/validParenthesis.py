class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        #Attempt 1
        # listA = []
        # listATwo = []
        # listB = []
        # listBTwo = []
        # listC = []
        # listCTwo = []
        # for i in s:
        #     if i == '(':
        #         listA.append(i)
        #     elif i == ')':
        #         listATwo.append(i)
        #     elif i == '[':
        #         listB.append(i)
        #     elif i == ']':
        #         listBTwo.append(i)
        #     elif i == '{':
        #         listC.append(i)
        #     elif i == '}':
        #         listCTwo.append(i)
        
        # if len(listA) != len(listATwo):
        #     return False
        # if len(listB) != len(listBTwo):
        #     return False
        # if len(listC) != len(listCTwo):
        #     return False

        # #Attempt 2 
        # s = ''.join(sorted(s))
        # lastIndexOfA = s.rfind(')')
        # lastIndexOfB = s.rfind(']')
        # lastIndexOfC = s.rfind('}')

        # # if (lastIndexOfA == -1 or lastIndexOfB == -1 or lastIndexOfC == -1):
        # #     return False

        # listA = s[0:lastIndexOfA+1]
        # listB = s[lastIndexOfA+1: lastIndexOfB+1]
        # listC = s[lastIndexOfB+1: len(s)]
        # print(listA)
        # print(listB)
        # print(listC)


        # if len(listA) == 1 or len(listB) == 1 or len(listC) == 1:
        #     return False

        # if len(listA)%2 != 0 or len(listB)%2 != 0 or len(listC)%2 != 0:
        #     return False

        #attmept 3
        brackets = ['(',')', '[', ']', '{', '}']
        if len(set(s)) == 1:
            return False
        stackList = []
        for i in range(len(s)):
            stackList.append(s[i])
            stackTop = stackList[len(stackList)-1]
            if len(stackList) > 1:
                stackBelow = stackList[len(stackList)-2]
                if stackTop == ')':
                    if stackBelow == '(':
                        stackList.pop()
                        stackList.pop()
                    else:
                        return False
                elif stackTop == ']':
                    if stackBelow == '[':
                        stackList.pop()
                        stackList.pop()
                    else:
                        return False
                elif stackTop == '}':
                    if stackBelow == '{':
                        stackList.pop()
                        stackList.pop()
                    else:
                        return False
                elif stackBelow == ')' or stackBelow == '}' or stackBelow == ']': 
                    return False
                # elif stackTop == '[' or stackTop == '(' or stackTop == '{':
                #     return False
            if s[len(s)-1] == '[' or s[len(s)-1] == '(' or s[len(s)-1] == '{':
                return False
        return True

def main():
    s =["()", "()[]{}", "(]", "([])","([)]", ")[]", "(["]
    for i in range(len(s)):
        print(s[i], " ", Solution().isValid(s[i]))

if __name__ == "__main__":
    main()  