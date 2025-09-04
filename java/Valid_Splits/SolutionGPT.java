package Valid_Splits;

public class SolutionGPT {
    public int waysToSplitArray(int[] nums) {
        int validSplitCount = 0;
        int n = nums.length;

        // Calculate the total sum of the array
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // Prefix sum to calculate left and right sums
        long prefixSum = 0;
        for (int i = 0; i < n - 1; i++) {
            prefixSum += nums[i]; // Update the prefix sum
            long rightSum = totalSum - prefixSum; // Calculate the right part's sum
            
            // Check if the left sum is greater than or equal to the right sum
            if (prefixSum >= rightSum) {
                validSplitCount++;
            }
        }

        return validSplitCount;
    }
    public static void main(String[] args) {
        Solution obj = new Solution();
        int[] arr = {-1,-2};
        System.out.println(obj.waysToSplitArray(arr));
    } 
}
