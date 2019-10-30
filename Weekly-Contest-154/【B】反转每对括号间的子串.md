> *题目原链接：[1190. 反转每对括号间的子串](https://leetcode-cn.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/)*

### 题目

给出一个字符串 `s`（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 **不应** 包含任何括号。

 

**示例 1：**

```
输入：s = "(abcd)"
输出："dcba"
```

**示例 2：**

```
输入：s = "(u(love)i)"
输出："iloveu"
```

**示例 3：**

```
输入：s = "(ed(et(oc))el)"
输出："leetcode"
```

**示例 4：**

```
输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
```

**提示：**

- `0 <= s.length <= 2000`
- `s` 中只有小写英文字母和括号
- 我们确保所有括号都是成对出现的

### 解析

首先可以注意到，需要按照 **从括号内到外** 的顺序，逐层反转，因此需要在处理最里面那对括号之前把前面的字符按一定规则存起来，而分割标识就是 `(`，只要遇到一个 `(`，就意味着从当前位置开始，到之后遇到的第一个 `)` 为止，其中的字符需要拼接反转，反转后的字符串可以拼接到上一个 `(` 包含的字符串后面，依次迭代下去即可将所有括号中的字符反转。

### 代码

```cpp
class Solution {
public:
    string reverseParentheses(string s) {
        vector<string> v(1);
        for (auto c : s) {
            if (c == '(') {
                v.push_back("");
            } else if (c == ')') {
                auto t = v.back();
                reverse(t.begin(), t.end());
                v.pop_back();
                v.back() += t;
            } else {
                v.back() += c;
            }
        }
        return v[0];
    }
};
```