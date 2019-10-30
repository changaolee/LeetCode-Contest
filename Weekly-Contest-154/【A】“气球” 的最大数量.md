> *题目原链接：[1189. “气球” 的最大数量](https://leetcode-cn.com/contest/weekly-contest-154/problems/maximum-number-of-balloons/)*

### 题目

给你一个字符串 `text`，你需要使用 `text` 中的字母来拼凑尽可能多的单词 "**balloon**"（气球）。

字符串 `text` 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "**balloon**"。

**示例 1：**

```
输入：text = "nlaebolko"
输出：1
```

**示例 2：**

```
输入：text = "loonbalxballpoon"
输出：2
```

**示例 3：**

```
输入：text = "leetcode"
输出：0
```

**提示：**

- `1 <= text.length <= 10^4`
- `text` 全部由小写英文字母组成

### 解析

统计字符串中 "**balloon**" 词的每个字母出现次数，返回其中的最小值即可。

注意：`l` 和 `o` 在原单词中出现两次，需要除以二统计出现了多少对。

### 代码

```cpp
class Solution {
public:
    int cnt[30];
    int maxNumberOfBalloons(string text) {
        memset(cnt, 0, sizeof(cnt));
        for (auto c: text) ++ cnt[c - 'a'];
        
        int ans = 1e5, cur = 0;
        int word[] = {'b', 'a', 'l', 'o', 'n'};
        for (auto c: word) {
            cur = (c == 'l' || c == 'o') ? cnt[c - 'a'] / 2 : cnt[c - 'a'];
            ans = min(ans, cur);
        }
        return ans;
    }
};
```