class Solution:
    def productExceptSelf(self, nums: list[int]):
        
        answer = []

        #prefixSum calculation (prefix product)
        tempnums = nums[::-1]
        prefixProduct = [nums[0]]
        suffixProduct = [nums[len(nums)-1]]
        print(suffixProduct)
        for i in range(1, len(nums)):
            prefixProduct.append(prefixProduct[i-1]*nums[i])
            suffixProduct.append(suffixProduct[i-1]*tempnums[i])
        print("Prefix Product: " , prefixProduct)
        suffixProductReversed = suffixProduct[::-1]
        print("Suffix Product: " , suffixProductReversed)
        suffixProductReversed.append(1)

        for i in range(len(nums)):
            answer.append(prefixProduct[i-1]*suffixProductReversed[i+1])

        return answer
def main():
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))    

if __name__ == "__main__":
    main()