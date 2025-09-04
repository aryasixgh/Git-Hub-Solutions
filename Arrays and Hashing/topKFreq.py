class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        freqDict = {}
        for i in nums: 
            if i not in freqDict:
                freqDict[i]=1
            else:
                freqDict[i]+=1
        answer = []
        print(freqDict)

        sortedDict = sorted(freqDict.items(), key=lambda item: item[1], reverse=True)
        print(sortedDict)
        for i in range(int(k)):
            answer.append(sortedDict[i][0])
        return answer

def main():
    # nums = input("nums: ")
    # k = input("k: ")
    # print(nums)
    # nums = nums.split()
    # print(nums)
    nums = [1, 1, 2, 1, 2, 3]
    k=2
    print(Solution().topKFrequent(nums, k))

if __name__ == "__main__":
    main()