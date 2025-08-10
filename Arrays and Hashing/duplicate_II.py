class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False

def main():
    nums = [1,0,1,1]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))

if __name__ == "__main__":
    main()