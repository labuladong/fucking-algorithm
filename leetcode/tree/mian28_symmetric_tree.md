
## question
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


输入：root = [1,2,2,3,4,4,3]
输出：true


输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
时间复杂度 O(N) ： 其中 NN 为二叉树的节点数量，每次执行 recur() 可以判断一对节点是否对称，因此最多调用 N/2 次 recur() 方法。
空间复杂度 O(N) ： 最差情况下（见下图），二叉树退化为链表，系统使用 O(N) 大小的栈空间



对称二叉树定义： 对于树中 任意两个对称节点 LL 和 RR ，一定有：
L.val = R.val：即此两对称节点值相等。
L.left.val = R.right.val ：即 LL 的 左子节点 和 RR 的 右子节点 对称；
L.right.val = R.left.val ：即 LL 的 右子节点 和 RR 的 左子节点 对称

作者：jyd
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _is_symmetric(right, left):
            if not right and not left: 
                return True
            elif not right or not left:
                return False
            elif  right.val == left.val:
                return _is_symmetric(right.right,left.left) and _is_symmetric(left.right,right.left)
            else:
                return False
        return _is_symmetric(root.right,root.left) if root else True
```