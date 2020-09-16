<!-- TOC -->

- [question](#question)
- [DFS](#dfs)

<!-- /TOC -->

## question
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。


输入：A = [1,2,3], B = [3,1]
输出：false


输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

通过次数19,982提交次数43,316
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



## DFS


算法思路(剑指offer):
第一步:在树A中找到和树B的根节点的值一样的节点R;
第二步:判断树A中以R为根节点的子树是不是包含和树B一样的结构
详细步骤:
第一步:在树A中查找与根节点的值一样的节点,这实际上就是树的遍历,可以使用递归或者循环实现,这个应该没什么问题,代码也有注释
第二步:判断树A中以R为根节点的子树是不是包含和树B一样的结构.同样我们使用递归来考虑:
如果节点R的值和树B的根节点不相同,则以R为根节点的子树和树B肯定不具有相同的节点
如果节点R的值和树B的根节点相同,则递归的判断他们各自左右节点的值是不是相同.递归的终止条件是达到了树A或者树B的叶节点
代码

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        result = False
        if  A and  B:#A和B都不为空
            if A.val == B.val:
                result = self.isSubTree(A, B)#递归的判断他们各自左右节点的值是不是相同
            if not result:
                result = self.isSubStructure(A.left, B)#不相等则将树A的左子树与B进行比较
            if not result:
                result = self.isSubStructure(A.right, B)#不相等则将树A的右子树与B进行比较
        return result

    def isSubTree(self, root_A, root_B):
        if not root_B:#如果B为空,说明前面的节点都能一一对应上了,所以B是A的子树
            return True
        if not root_A:#如果A为空,则说明B不是他的子树
            return False
        if root_A.val != root_B.val:#节点值不相等,说明也不是
            return False
        # 判断左右子树是否符合
        return self.isSubTree(root_A.left, root_B.left) and self.isSubTree(root_A.right, root_B.right

```
作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/pythonti-jie-si-lu-qing-xi-de-dfs-by-xiao-xue-66/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
