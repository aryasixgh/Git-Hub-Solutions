package misc;

import java.util.*;

class Solution {
    public Integer[] maxFloors(Integer[] arr) {
        Arrays.sort(arr, Collections.reverseOrder());
        System.out.println(Arrays.toString(arr));
        int bestLen = 1, len = 1, bestStart = 0, start = 0;
        for (int i = 1; i < arr.length; i++) {
            int diff = arr[i - 1] - arr[i];
            if (diff == 0 || diff == 1) {
                len++;
            } else {
                if (len > bestLen) {
                    bestLen = len;
                    bestStart = start;
                }
                start = i;
                len = 1;
            }
        }
        if (len > bestLen) {
            bestLen = len;
            bestStart = start;
        }
        return Arrays.copyOfRange(arr, bestStart, bestStart + bestLen);
    }

    public static void main(String[] args) {
        Integer inputArr[] = { 1, 5, 4, 3, 2, 1, 7 };
        Solution obj = new Solution();
        System.out.println(Arrays.toString(obj.maxFloors(inputArr)));

    }
}
