class Solution:
    def twoSum(self, numbers, target):
        startPoint = 0
        endPoint = len(numbers)-1
        for i in range(len(numbers)):
            for j in range(startPoint, endPoint):
                complement = target - numbers[i]
                pivot = int((len(numbers)/2)-1)
                if numbers[pivot] == complement:
                    return [pivot+1, i+1]
                elif numbers[pivot] > complement:
                    endPoint = pivot
                    startPoint = 0
                elif numbers[pivot] < complement:
                    endPoint = len(numbers)-1
                    startPoint = pivot
                    
def main():
    numbers=[2,3,4]
    target=6
    print(Solution().twoSum(numbers, target))
if __name__ == "__main__":
    main()
