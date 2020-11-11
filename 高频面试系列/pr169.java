/*
    使用Boyer-Moore Majority Vote Algorithm
    用count来计算一个元素出现的次数，碰到的元素和统计的元素不想等时count减1。
    如果count等于0，说明前面的元素出现的次数少于一半。因为majority是大于一半的，
    最终会找到一个元素是majority
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