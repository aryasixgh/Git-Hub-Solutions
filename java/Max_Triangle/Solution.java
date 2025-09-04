
class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        int size=blue+red;
        int ans=0;
        if(red==1 && blue==1)
            return 1;
        for(int i=0; i<size; i++){
            if(red>i && red<=blue){ 
                red--; 
            }
            else if(blue>i && blue<=red){
                blue--;
            }else{
                ans=i+2;
                break;
            }

            if(blue>i && blue<=red){
                blue--;
            }else if(red>i && red<=blue){
                red--;
            }else{
                ans=i+2;
                break;
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        Solution obj = new Solution();
        System.out.println(obj.maxHeightOfTriangle(9,4));
    }
}