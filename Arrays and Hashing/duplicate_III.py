from collections import deque
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        seen = deque()
        if indexDiff>len(nums)-1:
            return True
        if(indexDiff == len(nums)-1):
            if abs(nums[0]-nums[len(nums)-1]<=valueDiff):
                return True
        for i in range(indexDiff+1):
            seen.append(nums[i])

        for i in range(indexDiff, len(nums)):
            if (abs(seen[0]-seen[len(seen)-1])) <= valueDiff :
                return True
            if i<len(nums)-1:
                seen.append(nums[i+1])
            if len(seen)>indexDiff+1:
                seen.popleft()
        return False
def main():
    #test case 1
    # nums = [1,2,3,1]
    # indexDiff = 3
    # valueDiff = 0
    # #test case 6
    # nums = [1,2,5,6,7,2,4]
    # indexDiff = 4
    # valueDiff = 0
    # Test Case 5
    # nums = [1,2,1,1]
    # indexDiff = 1
    # valueDiff = 0
    #Test Case  = 1
    # nums = [1,5,9,1,5,9]
    # indexDiff = 2
    # valueDiff = 3   
    # test case 42/55
    nums = [1,2,2,3,4,5]
    indexDiff = 3
    valueDiff  = 0
    print(Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))

if __name__ == "__main__":
    main()