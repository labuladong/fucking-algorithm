## question
[剑指 Offer 36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 ![二叉搜索树](./sword36_二叉搜索树.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
![_双向链表](./sword36_双向链表.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
 

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。

## solution
排序链表： 节点应从小到大排序，因此应使用 中序遍历 “从小到大”访问树的节点；
双向链表： 在构建相邻节点（设前驱节点 prepre ，当前节点 curcur ）关系时，不仅应 pre.right = curpre.right=cur ，也应 cur.left = precur.left=pre 。
循环链表： 设链表头节点 headhead 和尾节点 tailtail ，则应构建 head.left = tailhead.left=tail 和 tail.right = headtail.right=head 。

考虑使用中序遍历访问树的各节点 curcur ；并在访问每个节点时构建 curcur 和前驱节点 prepre 的引用指向；中序遍历完成后，最后构建头节点和尾节点的引用指向即可。

算法流程：
dfs(cur): 递归法中序遍历；

* 终止条件： 当节点 curcur 为空，代表越过叶节点，直接返回；
* 递归左子树，即 dfs(cur.left) ；
* 构建链表：
    * 当 prepre 为空时： 代表正在访问链表头节点，记为 headhead 。
    * 当 prepre 不为空时： 修改双向节点引用，即 pre.right = curpre.right=cur ， cur.left = precur.left=pre ；
    * 保存 curcur ： 更新 pre = curpre=cur ，即节点 curcur 是后继节点的 prepre ；
* 递归右子树，即 dfs(cur.left) ；



treeToDoublyList(root)：
* 特例处理： 若节点 rootroot 为空，则直接返回；
* 初始化： 空节点 prepre ；
* 转化为双向链表： 调用 dfs(root) ；
* 构建循环链表： 中序遍历完成后，headhead 指向头节点， prepre 指向尾节点，因此修改 headhead 和 prepre 的双向节点引用即可。
* 返回值： 返回链表的头节点 headhead 即可。

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/sword-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```py
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
```

### code_me
```py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        _left, _right = self.get_node(root)
        _left.left = _right
        _right.right = _left
        return _left

    def get_node(self, node):
        if not node.right: 
            right = node
        else: 
            _left,right = self.get_node(node.right)
            _left.left = node
            node.right = _left
        if not node.left: 
            left = node
        else: 
            left,_right = self.get_node(node.left)
            _right.right = node
            node.left = _right
        return left,right
```