# 修正 labuladong 刷题插件中的错误

## 背景

为了帮助大家更好地学习算法，我之前写了很多算法教程，并开发了一系列刷题插件，统称为《labuladong 的刷题全家桶》，详情见 [这里](https://labuladong.github.io/article/fname.html?fname=全家桶简介)。

在我的教程和插件中的解法主要使用的是 Java 语言，原因是 Java 这门语言中规中矩，就算之前没有接触过，也能比较容易看懂逻辑。不过现在这不是 chatGPT 横空出世了嘛，我就借助 chatGPT 把我的解法改写成多种语言，希望对不同技术背景的小伙伴更加友好。

chatGPT 的改写效果还是非常不错的，不过难免还是存在一些错误，所以我希望能够和大家一起来修正这些错误。

## 如何反馈错误

如果你发现某些解法代码不能通过力扣的所有测试用例（一般都是 chatGPT 改写的解法代码会出现这种情况，我的解法代码都是通过测试才发布的），可以 [点这里](https://github.com/labuladong/fucking-algorithm/issues/new?assignees=&labels=code+bug&template=bug_report.yml&title=%5Bbug%5D%5B%7B%E8%BF%99%E9%87%8C%E6%9B%BF%E6%8D%A2%E4%B8%BA%E5%87%BA%E9%94%99%E7%9A%84%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80%7D%5D+%7B%E8%BF%99%E9%87%8C%E6%9B%BF%E6%8D%A2%E4%B8%BA%E5%87%BA%E9%94%99%E7%9A%84%E5%8A%9B%E6%89%A3%E9%A2%98%E7%9B%AE%E6%A0%87%E8%AF%86%E7%AC%A6%7D+) 按照模板提交 issue，我和其他小伙伴会提交 PR 修复这些错误。

## 如何修正错误

首先，感谢你愿意为我的插件提供的解法代码纠错，你向本仓库提交 PR 修复错误后，你将成为本仓库的 contributor，出现在仓库首页的贡献者列表中。本仓库已经获得了 115k star，你的贡献将会被许多人看到。

修复代码很简单，所有多语言解法代码都存储在 [多语言解法代码/solution_code.md](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%A4%9A%E8%AF%AD%E8%A8%80%E8%A7%A3%E6%B3%95%E4%BB%A3%E7%A0%81/solution_code.md) 中，你只要修改这个文件就行了。其内容的组织形如如下：


    https://leetcode.cn/problems/xxx 的多语言解法👇

    ```cpp
    class Solution {
    public:
        int xxx() {
            // ...
        }
    };
    ```

    ```java
    class Solution {
        public int xxx() {
            // ...
        }
    }
    ```

    ```python
    class Solution:
        def xxx(self):
            # ...
    ```

    ```javascript
    var xxx = function() {
        // ...
    }
    ```

    ```go
    func xxx() {
        // ...
    }
    ```

    https://leetcode.cn/problems/xxx 的多语言解法👆


比如你想修改 [https://leetcode-cn.com/problems/longest-palindromic-substring/](https://leetcode-cn.com/problems/longest-palindromic-substring/) 的 JavaScript 解法，你可以在 [多语言解法代码/solution_code.md](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%A4%9A%E8%AF%AD%E8%A8%80%E8%A7%A3%E6%B3%95%E4%BB%A3%E7%A0%81/solution_code.md) 中搜索 `longest-palindromic-substring` 关键词，即可找到这道题的多语言解法，然后修改 JavaScript 对应的解法代码，提交 PR 即可。

我的插件会自动拉取这个文件的最新内容，所以你的 PR 被合进 master 分支后，插件中的内容修改也会生效。

## 提交 PR 的要求

1、你的 PR 必须是针对 [多语言解法代码/solution_code.md](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%A4%9A%E8%AF%AD%E8%A8%80%E8%A7%A3%E6%B3%95%E4%BB%A3%E7%A0%81/solution_code.md) 文件中代码部分的修改，不要修改其他文件和其他内容。

2、把我的解法翻译成多语言的目的是帮助不同背景的小伙伴理解算法思维，所以你修改的代码可以不是效率最优的，但应该尽可能和我的解法思路保持一致，且包含我的解法中的完整注释。

3、你的 PR 描述中需要包含代码通过所有测试用例截图。PR 标题的格式为 `[fix][{lang}] {slug}`，其中 `{lang}` 需要替换为你修复的解法语言，比如 `[fix][cpp]`，`{slug}` 需要替换为你修复的题目的标识符（题目 URL 的最后一部分），比如 [https://leetcode.cn/problems/search-a-2d-matrix/](https://leetcode.cn/problems/search-a-2d-matrix/) 这道题的标识符就是 `search-a-2d-matrix`。

**你可以查看这个 PR 作为案例**：https://github.com/labuladong/fucking-algorithm/pull/1112