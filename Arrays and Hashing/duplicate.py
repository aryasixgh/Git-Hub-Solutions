class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        empty_dict = {}
        for i in nums:
            if i in empty_dict:
                return True
            empty_dict[i] = True
        return False
        
def main():
    sol = Solution()
    nums = [1, 2, 3, 2]
    print(sol.containsDuplicate(nums))

if __name__ == "__main__":
    main()
        
        