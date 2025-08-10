class Solution:
    def longestConsecutive(self, nums: list[int]):
        #ATTEMPT 1
        # nums = list(set(nums))
        # if len(nums) == 0:
        #     return 0
        # nums.sort()
        # finalList = []
        # print(nums)
        # for i in range(0, len(nums)-1):
        #     numOne = nums[i]
        #     numsTwo = nums[i+1]
        #     if nums[i+1]-nums[i] == 1 or nums[i+1]-nums[i] == -1:
        #         finalList.append(nums[i])
            
                
        # print(finalList)
        # return len(finalList)+1
        #ATTEMPT 2
        numSet = list(set(nums))
        longest = 0

        for i in nums:
            if (i-1) not in numSet:
                len = 1  
                while (i+len) in numSet:
                    len += 1
                longest = max(len, longest)
        return longest

def main():
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))

if __name__ == "__main__":
    main()