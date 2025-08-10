
class Solution():
    def slidingWindowSum(self, arr, k):
        maxSum = sum(arr[:k])
        ansSum = 0
        for i in range(1, len(arr)-k):
            ansSum = ansSum - arr[i-1] + arr[i+k-1]
            if maxSum < ansSum:
                maxSum = ansSum
        return maxSum

def main():
    arr = [5,2,-1,0,3]
    k = 3 
    print(Solution().slidingWindowSum(arr, k))

if __name__ == "__main__":
    main()