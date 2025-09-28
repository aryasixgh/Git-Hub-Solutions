package misc;

class primeSum {
    boolean checkPrime(int num) {
        boolean value = false;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                value = false;
                break;
            } else {
                value = true;
            }
        }
        return value;
    }

    int sum(int num) {
        int ans = 0;
        for (int i = 1; i <= num; i++) {
            if (checkPrime(i)) {
                ans += i;
            }
        }
        return ans + 2;
    }

    public static void main(String[] args) {
        primeSum obj = new primeSum();
        System.out.println("Ans = " + obj.sum(445));
    }
}
