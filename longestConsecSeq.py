class Solution:
    def longestConsecutive(self, nums: list[int]):
        if len(nums) == 0:
            return 0
        nums.sort()
        finalList = []
        for i in range(0, len(nums)-1):
            if nums[i+1]-nums[i] == 1 and nums[i] >= 0 and nums[i+1]>=0:
                finalList.append(nums[i])
            
                
        print(finalList)
        return len(finalList)+1

def main():
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(Solution().longestConsecutive(nums))

if __name__ == "__main__":
    main()