package Valid_Splits;

public class Solution {
    public int waysToSplitArray(int[] nums) {
        int validSplitCount=0;
        int n = nums.length;
        for(int i=0; i<n-1; i++){
            // int[] arr= new int[i+1];
            // int[] arr2 = new int[n-i-1];
            int j=0;
            int sumFirst=0;
            for(j=0; j<=i; j++){
                // arr[j]=nums[j];
                sumFirst+=nums[j];
            }

            //second half sum
            int sumSecond=0;
            for(int k=0; k<n-i-1; k++){
                // arr2[k]=nums[k+j];
                sumSecond+=nums[k+j];
            }
            if(sumFirst>=sumSecond){
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
