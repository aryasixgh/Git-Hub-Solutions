package misc;

public class reverseString {
    void reverse(String str) {
        String ansString = "";
        for (int i = str.length() - 1; i > 0; i--) {
            ansString += str.charAt(i);
        }
        System.out.println(ansString);
    }

    public static void main(String[] argss) {
        String inputString = "Hello, World";
        reverseString obj = new reverseString();
        obj.reverse(inputString);
    }
}
