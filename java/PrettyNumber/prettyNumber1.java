// Online Java Compiler
// Use this editor to write, compile and run your Java code online
class Solution {
    public String makeFancyString(String s) {
        char[] str=new char[s.length()];
        for(int i=0; i<s.length(); i++){
            str[i]=s.charAt(i);
        }
        for(int i=0; i<s.length()-1; i++){
            int count=0;
            for(int j=i; j<s.length(); j++){
                if(str[i]==str[j]){
                    count++;
                    System.out.println("Count: "+count+ 
                                        "\nstr[i]: "+str[i]+
                                        "\nstr[j]: "+str[j]);
                }
                if(count>=3){
                    str[j]=0;
                    System.out.println("Repalced");
                    break;
                }
            }
        }
        String newStr="";
        for(int i=0; i<s.length(); i++){
            newStr+=str[i];
        }
        System.out.println(newStr);
        return newStr;
    }
        public static void main(String[] args) {
            Solution obj=new Solution();
            String ans=obj.makeFancyString("aaabbcccaa");
            System.out.println(ans);
    }
}