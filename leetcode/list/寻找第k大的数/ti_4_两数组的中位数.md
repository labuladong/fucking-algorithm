
**有序数组中的第 k 小的数**
**二分法**

**重点，每次舍弃 k/2**
**这里 我们考虑 k/2 + k/4 + k/8 +k/16 + k/32 .... 这样就不断下去， 每次都舍弃 k/2, 其和最终就是 k .**

## question
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。


示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution
这里 主要是 对 官方答案的基础上， 说明下 自己见解。有不完整的可以参考 官方答案。

如何把时间复杂度降低到 O(log(m+n)) 呢？如果对时间复杂度的要求有 log，通常都需要用到二分查找，这道题也可以通过二分查找实现。

根据中位数的定义，当 m+n 是奇数时，中位数是两个有序数组中的第 (m+n)/2 个元素，当 m+n是偶数时，中位数是两个有序数组中的第 (m+n)/2 个元素和第 (m+n)/2+1 个元素的平均值。因此，这道题可以转化成寻找两个有序数组中的第 k 小的数，其中 k 为 (m+n)/2 或 (m+n)/2+1

想想如何在一个有序数组中找到第 k 个数。 这里 假设 从小到大的数组。单个数组 直接及时 A[k-1]
假设两个有序数组分别是 A 和 B。要找到第 k 个元素，我们可以比较A[k/2−1] 和 B[k/2−1]，其中 / 表示整数除法。

**重点，每次舍弃 k/2**
**这里 我们考虑 k/2 + k/4 + k/8 +k/16 + k/32 .... 这样就不断下去， 每次都舍弃 k/2, 其和最终就是 k .**
每次都 remove k/2 ， k = k-k/2, (注意这里是 k = k -k/2, 而不是 k= k/2)
k = 7, 当我们用 k=k/2 时： k=7, k/2 = 3, remove 3 ; k= k/2 =1, k/2=0 remove=0, k=0 ,这里总共 remove 3 ,还不到 7 。
k = 7, 当我们用 k=k- k/2 时： k=7, k/2 = 3, remove 3 ; k=k-k/2=4, k/2=2,remove=2; k=k-k/2=2, k/2 =1, remove=1;k=k-k/2=1,k/2=0,remove=0 这里总共 remove 3+2+1, 下一个就是我们需要的 7 。
详细可以看代码 ：

同理，写 y 分点
y = 2,3,4,5,6,....


# 这是 y分点  .
```py
    y=2
    all_len = len(nums1) + len(nums2)
    if all_len % y == 0:
        print (get_median(all_len / y + 1)*(y-1) + (get_median(all_len / y)))/float(y)
    else:
        x = all_len % y
        print ((get_median(all_len /y + 1)) * (y+1-x) + (x-1)*(get_median(all_len / y + 2))) / float(y)
```

```py
# -*- coding:utf-8 -*-

def findMedianSortedArrays(nums1, nums2):

    def get_median(k):
        init_K = k 
        move_1, move_2 = 0, 0
        while True:
            if move_1 >= len(nums1):  ## 第一个 list 比较短
                return nums2[init_K - len(nums1) -1]
            if move_2 >= len(nums2):   ## 第二个 list  比较短
                return nums1[init_K - len(nums2) -1]
            if k == 1:
                ## 之所以没有 index - 1， 是因为 k==1, 还有一个没有remove， 我们需要比较下一个。
                return min(nums1[move_1], nums2[move_2])

            ## 保证 index 在数组内。以免越界
            new_index1=max(1,(move_1+ k/2))
            new_index2=max(1,(move_2+ k/2))
            new_index1=min(len(nums1),new_index1)
            new_index2=min(len(nums2),new_index2)

            
                # like k = 7,move_1 = 0+7/2=3, k = k/2 =3 ;--we remove 3;     move_1 = 3+3/2=4, k = 3/2 =1,  we move 4; k/2 =0 ,so you go to judge , but all you remove is enough; less more 7.
                # like k = 7,move_1 = 0+7/2=3, k = k - k/2 =4 ;--we remove 3; move_1 = 3+4/2=5, k = 4/2 =2,  we move 5; move_1 = 5+2/2=6, k = 2/2 =1,  we move 6; k/2 = 0, index + k/2 == index, it is no need to do ;
                # so we set k = 1 to judge.; now we move 6, also need one to move, so  we use min(nums1[move_1], nums2[move_2]);in fact index had add 1.so it is ok
            if nums1[new_index1 - 1] <= nums2[new_index2 - 1]:
                move_1 = move_1+ k/2
                k = k - k/2
            else:
                move_2 = move_2+ k/2 
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-shu-zu-de-zhong-wei-shu-xun-zhao/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


```py
def findMedianSortedArrays(nums1, nums2):
    
    def get_element(k):
        in_k = k 
        last_1,last_2=0,0
        index_1,index_2=0,0
        move_k = k / 2

        while True:
            if move_k == 0:
                if k % 2 == 0:
                    return max(nums1[last_1-1],nums2[last_2-1])
                else:
                    return min(nums1[last_1-1],nums2[last_2-1])
            if last_1 > len(nums1):
                print "#2 ", nums2[(in_k - len(nums1) - 1)]
                return nums2[(in_k - len(nums1) - 1)]
            if last_2 > len(nums2):
                print "#3 ", nums1[(in_k - len(nums2) - 1)]
                return nums1[(in_k - len(nums2) - 1)]

            index_1 = min((index_1 + move_k -1 ),(len(nums1) -1))
            index_2 = min((index_2 + move_k -1 ),(len(nums1) -1))

            if nums1[index_1] < nums2[index_2]:
                last_1 = last_1 + move_k
                index_1 = index_1 + move_k 
                print "*",last_1  
            else:
                last_2 = last_2 + move_k
                index_2 = index_2 + move_k 
                print "**",last_2
            move_k = move_k / 2



    total_len = len(nums2) + len(nums1)

    if total_len % 2 == 0:
        print (get_element(total_len/2) + get_element(total_len/2 + 1))/2.0
    else:
        print get_element(total_len/2 + 1)


nums2 = [1,2,3]
nums1 = [3,4,5,6]
# nums2 = [1,2]
# nums1 = [3]
# nums2 = [1,2,3,4,5,6]
# nums1 = [0]
findMedianSortedArrays(nums1, nums2)
```