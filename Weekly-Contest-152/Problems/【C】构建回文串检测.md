> *题目原链接：[1177. 构建回文串检测](https://leetcode-cn.com/contest/weekly-contest-152/problems/can-make-palindrome-from-substring/)*

### 题目

给你一个字符串 `s`，请你对 `s` 的子串进行检测。

每次检测，待检子串都可以表示为 `queries[i] = [left, right, k]`。我们可以 **重新排列** 子串 `s[left], ..., s[right]`，并从中选择 **最多** `k` 项替换成任何小写英文字母。 

如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 `true`，否则结果为 `false`。

返回答案数组 `answer[]`，其中 `answer[i]` 是第 `i` 个待检子串 `queries[i]` 的检测结果。

注意：在替换时，子串中的每个字母都必须作为 **独立的** 项进行计数，也就是说，如果 `s[left..right] = "aaa"` 且 `k = 2`，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 `s`，可以认为每次检测都是独立的）

**示例：**

```
输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。
```

**提示：**

- `1 <= s.length, queries.length <= 10^5`
- `0 <= queries[i][0] <= queries[i][1] < s.length`
- `0 <= queries[i][2] <= s.length`
- `s` 中只有小写英文字母

### 解析

这里可以把解答分成三个步骤：

1. 尽可能短的时间内判断出 `left` 到 `right` 的数量为奇数的字符个数
2. 计算出所需要的改变次数
3. 和所给的 `k` 作对比

按以往的经验，若需要经常计算一个范围的值，可以采用前缀和。而前缀和的表示是该题目的难点之一，我们可以采用类似数位的方式来求得前缀和，并利用异或运算抵消那些数量为偶数的字符。

数位表示的方法：将数字的每一位看成一个字母，第一位看成 `a`，第二位看成 `b`，以此类推。如果存在该字母，则在对应的位置将其置为 `1` 。

前缀和计算：假如有字符串 `caa`，前两位的前缀和 `dp[1]` 则为 `101`。遍历到 `dp[2]` 时，我们只需要将 `dp[1]` 异或当前字符对应的数位即 `001`。

`101 ^ 001 = 100`，即消除了偶数数量的字符 `a`。

每次计算一个范围值时，继续利用异或运算。例如，`left` 到 `right` 的范围值为 `dp[right] ^ dp[left - 1]`。这是由于异或运算的性质，即相同元素异或之后会被清除。`dp[right]` 中包含 `0` 到 `left -1` 元素的影响，将其异或这些元素，即 `dp[left - 1]`，则可以消除影响。

此外，计算奇数数量字符时，我们可以使用 `n & (n - 1)` 快速将最右边的 `1` 置为 `0`。

### 代码

```cpp
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        vector<bool> ans;
        vector<int> dp(s.size() + 1);
        
        // 计算前缀和
        for (int i = 0; i < s.size(); i ++) {
            // 每个字符对应的数位,第 s[i] - 'a' 位置 1
            int num = 1 << (s[i] - 'a');
            dp[i + 1] = dp[i] ^ num;
        }
        
        for (auto iter = queries.begin(); iter != queries.end(); iter ++) {
            int start = (*iter)[0], end = (*iter)[1], k = (*iter)[2];
            // 通过前缀和计算范围值
            int cur = dp[end + 1] ^ dp[start];
            
            // 计算奇数字符的数量
            int cnt = 0;
            while (cur) {
                cur &= cur - 1;
                cnt += 1;
            }
            
            // 计算所需的改变次数
            if (cnt / 2 > k) ans.push_back(false);
            else ans.push_back(true);
        }
        
        return ans;
    }
};
```