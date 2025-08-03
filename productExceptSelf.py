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
            #suffixProduct.append(0)
            suffixProduct.append(suffixProduct[i-1]*tempnums[i])

        # suffixProduct.append(nums[len(nums)-1])
        # print(suffixProduct)

        # for i in range(len(suffixProduct)-2, -1, -1):
        #     suffixProduct[i]=(suffixProduct[i+1]*nums[i])
        print("Prefix Product: " , prefixProduct)
        suffixProduct.pop()
        suffixProductReversed = suffixProduct[::-1]
        print("Suffix Product Raw: ", suffixProduct)
        suffixProductReversed.append(1)        
        print("Suffix Product Reversed: " , suffixProductReversed)

        prefixProductReversed =  prefixProduct[::-1]
        prefixProductReversed.append(1)
        prefixProduct = prefixProductReversed[::-1]
        print(prefixProduct)

       #answer.append(suffixProductReversed[0])
        for i in range(len(nums)):
            answer.append(prefixProduct[i]*suffixProductReversed[i])

        return answer
def main():
    nums = [1,2,3,4]
    nums2 = [4,3,2,1,2] #[48,16,24,48,24] expected: [12,16,24,48,24]
    nums3 = [4, 3, 8, -9, 1]
    print(Solution().productExceptSelf(nums2))    

if __name__ == "__main__":
    main()