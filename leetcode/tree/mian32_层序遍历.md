from collections import deque
 _queue = deque([]) 
 
 _deque.leftpop() 
 _deque.append()

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        from collections import deque
        _all = deque([])
        _all.append(root)
        _res = []
        def _print(_all):
            _cur_list = []
            _cur_queue = deque([])
            while len(_all) >= 1 :
                _cur = _all.popleft()
                _cur_list.append(_cur.val)
                if _cur.left: _cur_queue.append(_cur.left)
                if _cur.right: _cur_queue.append(_cur.right)
            if _cur_list: _res.append(_cur_list)
            if len(_cur_queue) >= 1: 
                _print(_cur_queue)

        _print(_all)
        return _res
```

```py
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        from collections import deque
        _all = deque([])
        _all.append(root)
        _res = []
        def _print(_all):
            while len(_all) >= 1 :
                _cur = _all.popleft()
                _res.append(_cur.val)
                if _cur.left: _all.append(_cur.left)
                if _cur.right: _all.append(_cur.right)

        _print(_all)
        return _res
```
