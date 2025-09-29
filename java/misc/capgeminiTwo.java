package misc;

import java.util.Arrays;

public class capgeminiTwo {

    public static void main(String[] artgs) {
        int arr[] = { 5, 3, 4 };
        int p = 0;
        int increment = 0;
        while (Arrays.stream(arr).sum() != 0) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == p) {
                    arr[i] = 0;
                    p = 0;
                } else {
                    arr[i]--;
                    p++;
                }
            }
            increment++;
        }
        System.out.println(increment);
    }
}
