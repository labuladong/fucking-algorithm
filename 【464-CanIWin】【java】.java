class Solution {
    //本题的重复子问题：选某位选手选到1，3实际上和选到3，1的结果是一样的，故在不断选择时就会有很多重复子问题
    //hashtable是一种可行的判断key是否相同的数据结构，但是因为顺序不同，所以key值需要自己设计
    //于是设想一种选择顺序不影响对应的hash值的结构作为key
    //==>用Integer的二进制表示：32位bits，每一位的1/0代表本位置的数已选/未选
    //如：0001 0001代表index = 0、4的位置的数被选择了，即为数字1、5被选择了
    //这样，32位的Integer足够表示20以内的各个整数是否被选择。
    //dp[]用来保存选择这样的组合时，输赢状态
    
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if(desiredTotal <= 0) return true;
        if((maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal) return false;
        //根据maxChoosableInteger的不同来选择不同空间的dp，确保有足够的空间来保存某一个数是否被选择
        //如果某一数字i被选择了，则考虑更新规则
        //dp规则为：若本组数字被选了，且能赢，则更新为1；
        //         若本组数字被选了，但只能输，则更新为 -1；
        int[] dp = new int[1 << maxChoosableInteger];
        return helper(dp, maxChoosableInteger, desiredTotal, 0);
    }
    // 每做一次选择后T应减去相应值；state为已选则的数，初始为0表示尚未选择
    private boolean helper(int[] dp, int M, int T, int state){
        if(T <= 0) return false;
        if(dp[state] != 0) return dp[state] == 1; //若已有保存的状态，则直接判断其状态是否为能赢。
        //如何确定本次选择后的数字组合是什么？
        //为state^(1<<i)
        //例 0001 0001为现有state=17，本次选择3，则：
        //下次state为 0001 0001^(1 << 0000 0100) = 0001 0101
        //注意选择数字3，实际是1左移了3 - 1个位置，因为1本身为1 << 0, 
        //i从0开始循环，M-1为止，即为我们选的本数字为从1开始，到M为止
        for(int i = 0; i < M; i++){
            //若前一状态 与 本次选择的数 > 0,则说明本次选择的数已经被选择过了，不需要再选了，则继续下一循环
            if((state & (1 << i)) > 0) continue;
            
            //这里为何用！？因为自己选择后，即轮到对手选择，若自己选择后，到了对手的回合只能为false，则自己必为true能赢
            if(!helper(dp, M, T - (i + 1), state | (1 << i))){
                dp[state] = 1;
                return true;
            }
        }
        //若整个for循环过了都不能使对手必输而到达dp[state] = 1再return的状态，则本人必输
        dp[state] = -1;
        return false;
    }
}
