## question
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。


示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]


提示：
节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
## solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        _queue = []
        self.res = []
        self.k = sum        
        num = 0
        self.get_sum(root,0,_queue)
        return self.res

    def get_sum(self, node,_num,_queue):
        _queue.append(node.val)
        _num = _num + node.val
        if _num == self.k and not node.left and not node.right:     ## 必须到 叶节点
        # if _num == self.k:                                      ##  可以不到 叶节点
            self.res.append([i for i in _queue])               ### 这里是个 雷区， 当心
        if node.left: 
            self.get_sum(node.left,_num,_queue)
        if node.right: 
            self.get_sum(node.right,_num,_queue)
        if _queue: _queue.pop()

        

        
```