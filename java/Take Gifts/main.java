class Solution {
    public long pickGifts(int[] gifts, int k) {
        long sum=0;
        System.out.println("Hello World");
            for(int i=0; i<k; i++){
                int maxIndex=arrMax(gifts);
                gifts[maxIndex]=(int)Math.sqrt(gifts[maxIndex]);
            }
            for(int i=0; i<gifts.length; i++){
                sum+=gifts[i];
            }
        return sum;
    }
    int arrMax(int[] gifts){
        int maxIndex = 0;
        for (int i = 1; i < gifts.length; i++) {
            if (gifts[i] > gifts[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
    public static void main(String[]args){
        Solution obj=new Solution();
        System.out.println(obj.pickGifts(new int[] {54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72}, 7));

    }  
}