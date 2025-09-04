/*Keep Track of bracket open and close
 * swap when n(close) > n(open)
 * swap with opening bracket closest to the end of s
 * add a stoping clause (reint counts to 0 and repeat steps)
 * Note: This code has bad time complexity so really big strings cannot be computed
 * (Redundant code)
 */
class Solution {
    public int minSwaps(String s) {
        int iterationCount = 0;
        // convert string to character array
        char[] newString = s.toCharArray();
        for (int k = 0; k < s.length(); k++) {
            int closeCount = 0, openCount = 0;
            int firstCloseIndex = 0;
            for (int i = 0; i < s.length(); i++) {
                if (newString[i] == '[') {
                    openCount++;
                } else {
                    closeCount++;
                    firstCloseIndex = i;
                }
                //last index of
                int lastOpenIndex = s.lastIndexOf(']');
                if (closeCount > openCount) {
                    char temp = newString[firstCloseIndex];
                    newString[firstCloseIndex] = newString[lastOpenIndex];
                    newString[lastOpenIndex] = temp;
                    iterationCount++; // no of swaps
                    break; // after one swap is completed
                }
            }
        }
        return iterationCount;
    }

    public static void main(String[] args) {
        System.out.println("Start");
        Solution obj = new Solution();
        System.out.println(obj.minSwaps("]]][[["));
    }
}