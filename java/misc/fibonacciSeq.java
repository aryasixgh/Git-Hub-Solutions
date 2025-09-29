package misc;

public class fibonacciSeq {
    int recurssive(int i) {
        if (i <= 1) {
            return i;
        }
        return recurssive(i - 1) + recurssive(i - 2);

    }

    public static void main(String[] args) {
        fibonacciSeq obj = new fibonacciSeq();
        for (int i = 0; i < 10; i++) {
            System.out.print(obj.recurssive(i) + " ");
        }

    }
}
