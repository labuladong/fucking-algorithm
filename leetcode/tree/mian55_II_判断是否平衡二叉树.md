![image.png](https://pic.leetcode-cn.com/03ee0df6fa08bc95f420d94916317c974da2d32216159720698c02712e75b1f4-image.png)



## questions

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

给定二叉树 [3,9,20,null,null,15,7]

```sh
    3
   / \
  9  20
    /  \
   15   7
```
返回 true 。


给定二叉树 [1,2,2,3,3,null,null,4,4]

```sh
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```
返回 false 。

 

限制：

1 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



## solution

### 后序遍历

```py

# Definition for a binary tree node.

# class TreeNode(object):

# def __init__(self, x):

# self.val = x

# self.left = None

# self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self._flag = True           ##  类变量  记录 _flag
        print self._get_depth(root, 0)
        return self._flag

    def _get_depth(self, node, _dep):
        if not node: return True
        dep_r = self._get_depth(node.right, _dep + 1) if node.right else _dep  ## 记录 右边深度
        dep_l = self._get_depth(node.left, _dep + 1) if node.left else _dep     ## 记录左边深度
        # print "### ",dep_l, dep_r
        if (dep_l - dep_r) > 1 or (dep_r -dep_l) > 1: 
            self._flag = False                              ## 一旦有，就记录
        return dep_l if dep_l > dep_r else dep_r            ## 返回当前最大深度
```

```py
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1   ## -1 更有效， 且 此处判断，直接省时间。

        return recur(root) != -1

作者：jyd
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
### 先序遍历
```py
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```