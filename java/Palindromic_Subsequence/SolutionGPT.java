package Palindromic_Subsequence;

import java.util.HashSet;

public class SolutionGPT {
    public int countPalindromicSubsequence(String s) {
        int[] firstOccurrence = new int[26];
        int[] lastOccurrence = new int[26];
        int n = s.length();

        // Initialize first and last occurrences
        for (int i = 0; i < 26; i++) {
            firstOccurrence[i] = -1;
            lastOccurrence[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            int charIndex = s.charAt(i) - 'a';
            if (firstOccurrence[charIndex] == -1) {
                firstOccurrence[charIndex] = i;
            }
            lastOccurrence[charIndex] = i;
        }

        int palindromeCount = 0;

        // Check for unique palindromic subsequences
        for (int i = 0; i < 26; i++) {
            if (firstOccurrence[i] != -1 && firstOccurrence[i] < lastOccurrence[i]) {
                HashSet<Character> uniqueMiddleChars = new HashSet<>();
                for (int j = firstOccurrence[i] + 1; j < lastOccurrence[i]; j++) {
                    uniqueMiddleChars.add(s.charAt(j));
                }
                palindromeCount += uniqueMiddleChars.size();
            }
        }

        return palindromeCount;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int sol = obj.countPalindromicSubsequence("bbcbaba");
        System.out.println(sol); // Output: 4
    }
}
