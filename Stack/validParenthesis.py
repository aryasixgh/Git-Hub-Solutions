class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False        
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
            if s[len(s)-1] == '[' or s[len(s)-1] == '(' or s[len(s)-1] == '{':
                return False
        if len(stackList) != 0:
            return False
        return True

def main():
    s =["()", "()[]{}", "(]", "([])","([)]", ")[]", "([", "[[[]"]
    #s=["[[[]"]
    for i in range(len(s)):
        print(s[i], " ", Solution().isValid(s[i]))

if __name__ == "__main__":
    main()  