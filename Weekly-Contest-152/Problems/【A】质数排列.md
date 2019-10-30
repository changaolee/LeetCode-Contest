> *题目原链接：[1175. 质数排列](https://leetcode-cn.com/contest/weekly-contest-152/problems/prime-arrangements/)*

### 题目

请你帮忙给从 `1` 到 `n` 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 **模 mod** `10^9 + 7` 之后的结果即可。

 **示例 1：**

```
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
```

**示例 2：**

```
输入：n = 100
输出：682289015
```

**提示：**

- `1 <= n <= 100`

### 解析

首先需要注意的是，题目要求的放在「质数索引」上并不是每个质数要放在其对应的质数索引上，而是代表质数要放在任意一个质数索引上。

因此，`1` 到 `n` 的数进行排列时，质数的存放位置固定，只能放在质数索引上，而非质数的存放位置也是固定的，只能放在非质数索引上。对于 `n` 个数，`n` 个存放位置，排列的情况数为 `n!`。

### 代码

```cpp
class Solution {
public:
    const int MOD = 1e9 + 7;

    int numPrimeArrangements(int n) {
        int prime_cnt = 0, composite_cnt = 0;
        for (int i = 1; i <= n; i ++) {
            if (isPrime(i)) ++ prime_cnt;
            else ++ composite_cnt;
        }
        return (long) factorial(prime_cnt) * factorial(composite_cnt) % MOD;
    }
    
    int factorial(int num) {
        long ans = 1;
        for (int i = 2; i <= num; i ++) {
            ans = (ans * i) % MOD;
        }
        return ans;
    }
    
    bool isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i ++) {
            if (num % i == 0) return false;
        }
        return true;
    }
};
```