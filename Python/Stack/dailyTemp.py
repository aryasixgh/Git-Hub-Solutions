class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     tempStack = []
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             tempStack.append(temperatures[j])
        #             break
        #         else:
        #             tempStack.append(temperatures[j])
        #     if tempStack[0] < tempStack[len(tempStack)-1]:
        #        answer.append(len(tempStack)-1)
        #     else:
        #         answer.append(0)
        #     print(tempStack)
        stack = []
        for i in range(0, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                numero, indice = stack.pop()
                answer[indice] = i - indice
            stack.append((temperatures[i], i))

        return answer

def main():
    temperatures = [73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temperatures))

if __name__ == "__main__":
    main()