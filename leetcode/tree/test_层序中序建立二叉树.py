# -*- coding: UTF-8 -*-
## solution_in_layer
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, layer_order):
        """
        :type inorder: List[int]
        :type layer_order: List[int]
        :rtype: TreeNode
        """
        if len(layer_order) == 0:
            return None
        
        # 根节点
        # print "### in__layer 1 ",inorder
        # print "### in__layer 2 ",layer_order
        root = TreeNode(layer_order[0])
        # 获取根节点在 inorder 中的索引
        idx_root = inorder.index(layer_order[0]) 
        inorder_l = inorder[:idx_root]         # 就是左 子树 
        if len(inorder) > idx_root +1: 
            inorder_r = inorder[idx_root+1:]       # 就是 右子树
        else:
            inorder_r = None
        
        layer_l, layer_r = [], []
        for i in range(1,len(layer_order)):
            if layer_order[i] in inorder_l:
                layer_l.append(layer_order[i])
            else:
                layer_r.append(layer_order[i])
        root.left =  self.buildTree(inorder_l, layer_l) if layer_l else None
        root.right =  self.buildTree(inorder_r, layer_r) if layer_r else None
        if root.right and root.left:
            print "####",root.val,root.left.val,root.right.val
        return root

    def per_order(self,node):
        if not node: return []
        res = [node.val]
        res_l = self.per_order(node.left)
        res_r = self.per_order(node.right)
        res = res + res_l + res_r
        return res



layer = ["a1","b1","b2","c1","c2","c3","c4","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5"]
inorder = ["e1","d1","e2","c1","d2","b1","d3","c2","d4","a1","e3","d5","e4","c3","d6","b2","d7","c4","d8","e5"]
 
c =  Solution()
a = c.buildTree(inorder,layer)

print c.per_order(a)
