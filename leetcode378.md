<img width="1436" alt="378" src="https://user-images.githubusercontent.com/43448174/100830909-ad927d80-3432-11eb-85ea-0fc8cd6f46bd.png">

class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int lo = matrix[0][0];
        int hi = matrix[n-1][n-1];
        while(lo < hi){
            int mid = lo + (hi - lo)/2;
            //如果小于等于mid的个数小于k，那么lo = mid + 1 往前走一个
            if(equalOrsmaller(matrix,mid) < k){
                lo = mid + 1;
            }else{
                hi = mid; //如果等于大于或者等于k，那么hi就有可能是答案
            }
        }
        return lo;
    }
    //如果一个二维数组是有序的，若想小于等于某个特定值x的数量有多少个，
    //那么就从数组的左下角出发，如果matrix[i][j]<= x
    //则代表，从第0行到第i行的数字都小于等于x，我们可以increment j by 1；
    //如果不是，那么需要 i - 1，来找到更小的行。
    public int equalOrsmaller(int[][] matrix, int x){
        int n = matrix.length;
        int i = n - 1;
        int j = 0;
        int count = 0;
        while(i >= 0 && j < n){
            if(matrix[i][j] <= x){
                count += (i+1);
                j+=1;
            }else{
                i-=1;
            }
        }
        return count;
    }
}
