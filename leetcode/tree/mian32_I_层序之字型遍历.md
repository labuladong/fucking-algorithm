_sort ^= 1
from collections import deque

## question
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
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
        _sort = 0
        def _print(_all,_sort):
            _cur_list = []
            _cur_queue = deque([])
            if _sort == 0:
                while len(_all) >= 1 :
                        _cur = _all.popleft()
                        _cur_list.append(_cur.val)
                        if _cur.left: _cur_queue.append(_cur.left)
                        if _cur.right: _cur_queue.append(_cur.right)
            else:
                while len(_all) >= 1 :
                    _cur = _all.pop()
                    _cur_list.append(_cur.val)
                    if _cur.right: _cur_queue.appendleft(_cur.right)
                    if _cur.left: _cur_queue.appendleft(_cur.left)

            _sort ^= 1
            if _cur_list: _res.append(_cur_list)
            if len(_cur_queue) >= 1: 
                _print(_cur_queue,_sort)

        _print(_all,_sort)
        return _res
```