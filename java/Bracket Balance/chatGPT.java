class chatGPT {
    public int minSwaps(String s) {
        int balance = 0; // Tracks balance of brackets
        int swaps = 0; // Tracks the number of swaps required

        for (char c : s.toCharArray()) {
            if (c == '[') {
                balance++; // Increment for an open bracket
            } else {
                balance--; // Decrement for a close bracket
            }

            // If balance becomes negative, we need a swap
            if (balance < 0) {
                swaps++;
                balance = 0; // Reset balance after fixing the imbalance
            }
        }

        return swaps;
    }

    public static void main(String[] args) {
        chatGPT obj = new chatGPT();
        String s = "]]][[[";
        System.out.println("Minimum Swaps: " + obj.minSwaps(s));
    }
}
