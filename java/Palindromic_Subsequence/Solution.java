package Palindromic_Subsequence;
import java.util.Vector;

public class Solution {
    public int countPalindromicSubsequence(String s) {
        //Find Subsequences 
        //check if Palindromes
        //dont enter duplicate subsequences
        //String[] arr=new String[(int)Math.pow(2, s.length())];
        
        Vector<String> vec=new Vector<>();
        int len=s.length();
        for(int i=0; i<len; i++){
            for(int j=1+i; j<len; j++){
                for(int k=1+j; k<len; k++){
                    String str=s.charAt(i)+""+s.charAt(j)+""+s.charAt(k);
                    if(vec.contains(str)==false){
                        vec.addElement(str);
                    }
                }
            }
        }
        // for(String i:vec){
        //     System.out.print(i+" ");
        // }
        int palindromeCount=0;
        for(String i:vec){
            String rev="";
            //reversing
            int j=i.length()-1;
            while(j>=0){
                rev+=i.charAt(j)+"";
                j--;
            }
            if(i.equals(rev)){
                palindromeCount++;
            }
        }

        return palindromeCount;
    }
    public static void main(String[] args) {
        Solution obj=new Solution();
        int sol=obj.countPalindromicSubsequence("bbcbaba");
        System.out.println(sol);
    }
}
