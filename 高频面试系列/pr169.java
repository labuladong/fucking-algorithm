/*
    使用Boyer-Moore Majority Vote Algorithm
*/
class Solution {
    public int majorityElement(int[] nums) {
        int count = 1;
        int me = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                me = nums[i];
            }
            if (me == nums[i]) {
                count++;
            }
            else {
                count--;
            }
        }
        return me;
    }
}