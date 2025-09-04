// Input: words = ["mass","as","hero","superhero"]
// Output: ["as","hero"]

package String_Matching;
import java.util.ArrayList;
import java.util.List;
public class Solution {
        public List<String> stringMatching(String[] words) {
            List<String> listHere = new ArrayList<String>();
            
            for(String s : words){
                for(String s2 : words){
                    for(int i=0; i<s2.length(); i++){
                        String subString = s2.substring(0, i);
                        if (s.equals(subString)){
                            listHere.add(s);
                        }
                    } 
                }
            }
            
            return listHere;
    }
    public static void main(String[] args) {
        Solution obj = new Solution();
        System.out.println("Asnwer");
        String[] words = {"as", "hero", "superhero", "mass"};
        List<String> answer = obj.stringMatching(words);
        for(String str:answer){
            System.out.println(str);
        }
    }
}
