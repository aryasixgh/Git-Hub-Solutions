package attempt1;

/*Keep Track of bracket open and close
 * swap when n(close) > n(open)
 * swap with opening bracket closest to the end of s
 * add a stoping clause (reint counts to 0 and repeat steps)
 * Note: This code has bad time complexity so really big strings cannot be computed
 * (Redundant code)
 */
class mainnew {
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
                int lastOpenIndex = s.lastIndexOf('[');
                //old method
                /*
                for (int j = s.length() - 1; j >= 0; j--) {
                    if (newString[j] == '[') {
                        lastOpenIndex = j;
                        System.out.println("LOI = " + lastOpenIndex);
                        break;
                    }
                }*/
                //s.lastindex method fails because s is always the original string

                if (closeCount > openCount) {
                    char temp = newString[firstCloseIndex];
                    newString[firstCloseIndex] = newString[lastOpenIndex];
                    newString[lastOpenIndex] = temp;
                    iterationCount++; // no of swaps
                    //swapping char array back to string to retreive new last index
                    s = new String(newString);
                    break; // after one swap is completed
                }
            }
        }
        return iterationCount;
    }

    public static void main(String[] args) {
        System.out.println("asd");
        mainnew obj = new mainnew();
        System.out.println(obj.minSwaps(""));
    }
}