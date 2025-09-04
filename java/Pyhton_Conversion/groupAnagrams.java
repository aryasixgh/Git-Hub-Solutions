package Pyhton_Conversion;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class groupAnagrams {
    public List<List<String>> groupAnagramsFunciton(String[] strs) {

        Set<String> inputSet = new HashSet<>();
        for (int i = 0; i < strs.length; i++) {
            inputSet.add(strs[i]);
        }
        System.out.println("Inputt set " + inputSet);
        List<List<String>> li = new ArrayList<>();
        return li;
    }

    public static void main(String[] args) {
        groupAnagrams obj = new groupAnagrams();
        String[] strs = { "eat", "tea", "tan", "ate", "nat", "bat", "eat" };
        System.out.println(obj.groupAnagramsFunciton(strs));
    }
}
