import time
start = time.time()
class Solution:
    def twoSum(self, nums, target):
        # seen = [nums[0]]
        # for i in range(1, len(nums)):
        #     ans = nums[i]+seen[0]
        #     seen.append(nums[i])
        #     if ans == target:
        #         ind = len(nums) - 1 - nums[::-1].index(seen[0])
        #         ansList = [nums.index(nums[i]), ind]
        #         return ansList
        #     else:
        #         seen.pop(0)
        # -----Second Try------
        # hashMap = {}
        # for i in range(len(nums)):
        #     for j in range(len(nums)):     
        #         if i != j:   
        #             if nums[j] not in hashMap.values():
        #                 if nums[i]+nums[j] == target:
        #                     ansList = [i, j]
        #                     return ansList
        #             else:
        #                 hashMap[j] = nums[j]
        #-----Third Try-------
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                ansList = [dict[target-nums[i]], i]
                return ansList
            dict[nums[i]] = i
def main():
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))
    end =time.time()
    print("Time: ", (end-start), " seconds")
if __name__ == "__main__":
    main()