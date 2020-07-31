**异或 ^=**
<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 
示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
对应了 5 个元音每个次数或奇或偶一共 32 种状态
异或运算部分：
遍历字符串，从起始 pattern，也就是 0 开始，不断根据对应情况做异或运算
如果出现的是辅音，不进行异或运算
如果出现的是元音，根据元音种类分别对应做异或运算
答案更新：
如果当前的 pattern 没有出现过，那么以这个 pattern 为键，记录下当前位置，也就是索引的位置
如果出现过，那么更新目标长度：

```py
class Solution(object):
    def findTheLongestSubstring(self, s):
        mapper = {"a": 1,"e": 2,"i": 4,"o": 8,"u": 16}
        current_num = 0
        all_set_sort_dict = {0:-1}  ## 在所有list的开始之前， -1， 
        max_len,current_len=0,0
        for i in xrange(len(s)):
            if s[i] in mapper:
                current_num ^= mapper[s[i]]
                if current_num in all_set_sort_dict.keys():
                    current_len = i - all_set_sort_dict[current_num]
                else:
                    all_set_sort_dict[current_num] = i
                    current_len = 0
            else:
                current_len = i - all_set_sort_dict[current_num]
            if current_len > max_len:
                max_len = current_len
        return max_len
```
下面一种更容易理解， 直接用 dict ,
若排序不一，如[a,e] 与 [e,a]，将导致一些计算有差。因此增加一个 list.sort()

```py
class Solution(object):
    def findTheLongestSubstring(self, s):
        all_set_sort_dict = {}
        all_set_sort_dict['[]'] = -1
        current_list = []
        vowel_str="aeiou"
        max_len,current_len=0,0
        for i in xrange(len(s)):
            if s[i] in vowel_str:
                if s[i] not in current_list:
                    current_list.append(s[i])
                else:
                    current_list.remove(s[i])
                current_list.sort()
                _current_list=str(current_list)
                if _current_list in all_set_sort_dict.keys():
                    current_len = i - all_set_sort_dict[_current_list]
                else:
                    all_set_sort_dict[_current_list] = i
                    current_len = 0
            else:
                current_list.sort()
                _current_list=str(current_list)
                current_len = i - all_set_sort_dict[_current_list]
            if current_len > max_len:
                max_len = current_len
        return max_len
        ```

作者：mu-xie-a
链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/qian-zhui-he-yi-huo-yun-suan-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。