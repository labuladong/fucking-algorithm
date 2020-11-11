class Solution {
    public boolean judgeSquareSum(int c) {
        /* 
            如果小于或等于2，那么一定是2个数平方的和
            0^2 + 0^2 = 0, 1^2 + 0^2 = 1, 1^2 + 1^2 = 2
            Math.sqrt(c) % 1 == 0 是用来确认c是不是某个数的平方
            因为另一个数可以是0^2
        */
        if (c <= 2 || Math.sqrt(c) % 1 == 0) {
            return true;
        }
        
        /* 
            使用双指针， 两个平方的和必定在 i-j之间
        */
        int i = 1;
        int j = (int)Math.floor(Math.sqrt(c));
        while (i <= j) {
            if (c - j*j == i*i) {
                return true;
            }
            else if (c - j*j > i*i) {
                i++;
            }
            else {
                j--;
            }
        }
        return false;
    }
}