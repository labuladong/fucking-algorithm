**题目要求的 “序列化” 和 “反序列化” 是 可逆 操作。因此，序列化的字符串应携带 “完整的” 二叉树信息，即拥有单独表示二叉树的能力。**
**为使反序列化可行，考虑将越过叶节点后的 nullnull 也看作是节点。在此基础上，对于列表中任意某节点 nodenode ，其左子节点 node.leftnode.left 和右子节点 node.rightnode.right 在序列中的位置都是 唯一确定 的。**

作者：jyd
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [后序遍历](#%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86)

<!-- /TOC -->

![image.png](https://pic.leetcode-cn.com/e84b8204771ea637118ab53b4fdf86ecbf5dfdb51e0979203c6fd85e13ced8b2-image.png)

## question
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution


### 后序遍历
自己写
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:return []
        self.res = []
        def _code(node):
            if not node:
                self.res.append('null')
            if node.left:
                _code(node.left)
            else:
                self.res.append('null')
            if node.right:
                _code(node.right)
            else:
                self.res.append('null')
            self.res.append(node.val)
        _code(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == []: return
        _data = data
        def _decode(_data):
            if _data[-1] == 'null':
                _data.pop()
                return
            node = TreeNode(_data[-1])
            _data.pop()
            node.right=_decode(_data)
            node.left=_decode(_data)
            return node 
        return _decode(_data)
```

### 先序遍历

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        result = []
        def encodes(root):
            if not root:
                result.append('$')
                return
            result.append(root.val)
            encodes(root.left)
            encodes(root.right)
        encodes(root)
        return result

                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        index = [0] #全局变量
        def decodes(data):
            if data[index[0]] == '$':
                index[0] += 1
                return None
            node = TreeNode(data[index[0]])
            index[0] += 1
            node.left = decodes(data)
            node.right = decodes(data)
            return node
    
        return decodes(data)
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/pythonti-jie-qian-xu-bian-li-jie-fa-jian-dan-yi-do/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

### 层序遍历
```py
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

作者：jyd
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```