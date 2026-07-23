class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n < 3) {
            return n;
        }
        int bitLength = 32 - Integer.numberOfLeadingZeros(n);
        return 1 << bitLength;
    }
}
