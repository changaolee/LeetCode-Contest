> *题目原链接：[1178. 猜字谜](https://leetcode-cn.com/contest/weekly-contest-152/problems/number-of-valid-words-for-each-puzzle/)*

### 题目

外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

字谜的迷面 `puzzle` 按字符串形式给出，如果一个单词 `word` 符合下面两个条件，那么它就可以算作谜底：

单词 `word` 中包含谜面 `puzzle` 的第一个字母。
单词 `word` 中的每一个字母都可以在谜面 `puzzle` 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 `answer`，数组中的每个元素 `answer[i]` 是在给出的单词列表 `words` 中可以作为字谜迷面 `puzzles[i]` 所对应的谜底的单词数目。

**示例：**

```
输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
```

**提示：**

- `1 <= words.length <= 10^5`
- `4 <= words[i].length <= 50`
- `1 <= puzzles.length <= 10^4`
- `puzzles[i].length == 7`
- `words[i][j]`, `puzzles[i][j]` 都是小写英文字母。
- 每个 `puzzles[i]` 所包含的字符都不重复。

### 解析

首先看这道题，最普通的思路是对每个 `puzzle`，都对 `words` 遍历一遍，方法很直观，但一定超时。`words.length * puzzles.length` 会达到 `10^9`。

那么问题主要是，用怎么样的一种方法可以大大缩短时间？

1. 对于 `word`，其实每个 `word` 代表了一种模式，`abc` 和 `aaaaabbbccc` 是等价的。 我们需要提取出这种模式，可以使用位运算，将一个 `word` 用数位表示。
2. 对于一个 `puzzle`，有两种遍历谜底的思路。 一是遍历 `words`，另一种是遍历自己的模式子集。题目给我们的暗示是 `puzzles[i].length == 7`。这就意味着一个 `puzzle` 的模式，子集不会超过 `2^7 =128`，因此我们遍历 `puzzle` 模式的子集，采用 `map` 映射的方式统计谜底个数。

这里有一个计算子集的技巧，可以大大降低代码复杂度，`for (int j = cur; j; j = (j - 1) & cur) {}`，其中 `cur` 是 `puzzle` 的数位表示。

如：要遍历的 `cur = 0101`，则遍历的数据为 `0101`、`0100`、`0001`。

### 代码

```cpp
class Solution {
public: 
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        vector<int> ans(puzzles.size());
        map<int, int> bit2cnt;
        
        // 统计每个 word 模式的数量, map 形式保存, 位运算进行操作
        for (int i = 0; i < words.size(); i ++) {
            int cur = 0;
            for (int j = 0; j < words[i].size(); j ++) {
                cur |= (1 << (words[i][j] - 'a'));
            }
            bit2cnt[cur] += 1;
        }
        
        for (int i = 0; i < puzzles.size(); ++i) {
            int cur = 0;
            for (int j = 0; j < puzzles[i].size(); ++j) {  // 将 puzzles 的字符串转化为一个数字
                cur |= (1 << (puzzles[i][j] - 'a'));
            }
            // 遍历该数字出现 1 的子集
            for (int j = cur; j; j = (j - 1) & cur) {
                // 判断首字母是否为 1
                if ((1 << (puzzles[i][0] - 'a')) & j) {
                    ans[i] += bit2cnt[j];
                }
            }
        }
        return ans;
    }
};
```