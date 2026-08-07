class Solution {
    public int smallestNumber(int n, int t) {
        int current = n;
        while (true) {
            if (digitProduct(current) % t == 0) {
                return current;
            }
            current++;
        }
    }
    
    private int digitProduct(int num) {
        int prod = 1;
        while (num > 0) {
            int digit = num % 10;
            prod *= digit;
            num /= 10;
        }
        return prod;
    }
}
