**类变量来维护k和_res， self.k, self._res.**



## question
给定一棵二叉搜索树，请找出其中第k大的节点。


输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4


输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：
1 ≤ k ≤ 二叉搜索树元素个数


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self._res =''
        self.k = k
        self._des(root)
        return self._res

    def _des(self, node):
        if not node: return null
        if node.right: self._des(node.right)
        self.k = self.k - 1
        if self.k == 0: 
            self._res = node.val
            return 
        if node.left: self._des(node.left)
```
上面代码的核心是采用了 **类变量来维护k和_res， self.k, self._res.**
想让此次遍历结束，就用return 即可

二叉搜索树有一个很重要的特性：树中任何结点的左子树中所有结点的值均比该结点小，右子树中所有结点的值均比该结点大。对二叉搜索树进行中序遍历即得到一个递增排序的序列。

中序遍历 为 “左、根、右” ：  递增序列
```py   
# 打印中序遍历
def dfs(root):
    if not root: return
    dfs(root.left)  # 左
    print(root.val) # 根
    dfs(root.right) # 右
```

中序遍历的倒序 为 “右、根、左”     递减序列
```py
# 打印中序遍历倒序
def dfs(root):
    if not root: return
    dfs(root.right) # 右
    print(root.val) # 根
    dfs(root.left)  # 左
```
作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



```