class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '/' and i != '*':
                stack.append(i)
            else:
                temp1 = int(stack[len(stack)-1])
                temp2 = int(stack[len(stack)-2])
                stack.pop()
                stack.pop()
                if i == '+':
                    stack.append(temp1 + temp2)
                elif i == '-':
                    stack.append(temp2 - temp1)
                elif i == '/':
                    stack.append(temp2/temp1)
                elif i == '*':
                    stack.append(temp1*temp2)

        return int(stack[0])

def main():
    expression =["4","3","-"]
    print(Solution().evalRPN(expression))

if __name__ == "__main__":
    main()