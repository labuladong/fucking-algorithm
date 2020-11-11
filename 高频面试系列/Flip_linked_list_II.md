反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

```java
class Solution {
   ListNode startNode;
   ListNode endNode;
   ListNode startNodeNext;
   ListNode endNodeNext;
    public  ListNode reverseBetween(ListNode head, int m, int n) {
        if (head ==null) return null;
        m++;
        n++;
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;//添加一个伪头，这样可以统一操作，避免m=1时的特例考虑
        ListNode node = fakeHead;
        for (int i = 1; i <m-1 ; i++) {
            node = node.next;//遍历一半
        }
        startNode = node;
        startNodeNext = startNode.next;
        recur(node.next,node,m,n);//递归遍历另外一半
        startNode.next = endNode;
        startNodeNext.next = endNodeNext;
        return fakeHead.next;

    }
    /**
     * @param now 当前节点
     * @param pre 当前节点的前一个节点，当前节点是由这个节点递归来的
     * @param level 当前所在的层级
     * @param target 目标要达到的层级
     */
    public void recur(ListNode now,ListNode pre,int level,int target){
        if (level == target) {
            endNode = now;
            endNodeNext = endNode.next;
        }else recur(now.next,now,level+1,target);
        now.next = pre;

    }
}
```

![image-20201102210830177](E:\code\fucking-algorithm\pictures\Flip_linked_list.png)