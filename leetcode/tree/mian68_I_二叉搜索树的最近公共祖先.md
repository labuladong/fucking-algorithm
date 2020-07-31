**深度优先， 后序遍历**

![image.png](https://pic.leetcode-cn.com/ae7f631400307406dbc85a28d9e032e7c704e30ed813a618cea67243587dcec2-image.png)

时间复杂度 有点 吓人



## question
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]


输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。


输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



## solution


### 别人的
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if not root: return True
        return _islow(root,p,q)

## 从上到下找到第一个在两个输入节点值之间的节点就是最近的公共祖先

def _islow(node,p,q):
    if node.val < p.val and node.val < q.val:       ## 得利  于 二叉搜索树的  定义。
        return _islow(node.right,p,q)   ## 在 右边
    if node.val > p.val and node.val > q.val:
        return _islow(node.left,p,q)    ## 在 左边

    return node                         ## 既不在左，也不在右 ，那就是自己。
```


### 自己做
**深度优先， 后序遍历**

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if not root:return null
        return _rev_all(root,p,q)

def _rev_all(node,a,b):
    if node.right:
        __no = _rev_all(node.right, a,b)
        if __no: return __no  ## 深度优先， 后序遍历
    if node.left:
        __no = _rev_all(node.left, a,b)
        if __no :return __no
    if _isIn(node,a) and _isIn(node,b): 
        return node

    
def _isIn(big,small): ## 二叉搜索树   判断是否为 子节点。 (含 等于)
    if big.val > small.val:
        if big.left: return _isIn(big.left,small)
    if big.val < small.val:
        if big.right: return _isIn(big.right,small)
    return True if big.val == small.val else False  ## 相等的时候 也可以
    
    
    
```
```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """'''  '''
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if not root: return True
        return _islow(root,p,q)

def _islow(node,p,q):
    if node.val < p.val and node.val < q.val:       ## 得利  于 二叉搜索树的  定义。
        return _islow(node.right,p,q)   ## 在 右边
    if node.val > p.val and node.val > q.val:
        return _islow(node.left,p,q)    ## 在 左边

    return node                         ## 既不在左，也不在右 ，那就是自己。



```


## 一般二叉树

```py
如果是一般的二叉树，就一定要判断到节点为p或者q为止


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果当前节点为空，就返回空
        if not root:
            return None
        # 如果当前结点就是p或者q，就返回当前节点
        if root in [p, q]:
            return root
        
        # 分别去左右子树里面去找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树里各有一个p或者q，那么当前就是最前结点
        if left and right:
            return root

        # 如果都在左边，那就是当前这个左边的
        elif left:
            return left
        
        # 要么就是右边的
        elif right:
            return right
        
        return None

作者：EthanNING
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/python-di-gui-jie-fa-fu-dai-yi-ban-er-cha-shu-jie-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```