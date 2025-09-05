class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []
        for i in range(len(temperatures)):
            tempStack = []
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    tempStack.append(temperatures[j])
                    break
                else:
                    tempStack.append(temperatures[j])
            if tempStack[0] < tempStack[len(tempStack)-1]:
               answer.append(len(tempStack)-1)
            else:
                answer.append(0)
            print(tempStack)

        return answer

def main():
    temperatures = [30,60,90]
    print(Solution().dailyTemperatures(temperatures))

if __name__ == "__main__":
    main()