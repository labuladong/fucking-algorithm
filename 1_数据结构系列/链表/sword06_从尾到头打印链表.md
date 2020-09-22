
## question
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


输入：head = [1,3,2]
输出：[2,3,1]
 

限制：
0 <= 链表长度 <= 10000

通过次数45,244提交次数59,566
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution

```py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack, h = [], head
        while h:
            stack.append(h.val)
            h = h.next
        return stack[::-1]
```