> *题目原链接：[1191. K 次串联后最大子数组之和](https://leetcode-cn.com/contest/weekly-contest-154/problems/k-concatenation-maximum-sum/)*

### 题目

给你一个整数数组 `arr` 和一个整数 `k`。

首先，我们要对该数组进行修改，即把原数组 `arr` 重复 `k` 次。

举个例子，如果 `arr = [1, 2]` 且 `k = 3`，那么修改后的数组就是 `[1, 2, 1, 2, 1, 2]`。

然后，请你返回修改后的数组中的最大的子数组之和。

注意，子数组长度可以是 `0`，在这种情况下它的总和也是 `0`。

由于 **结果可能会很大**，所以需要 **模（mod）** `10^9 + 7` 后再返回。 

`示例 1：`

```
输入：arr = [1,2], k = 3
输出：9
```

**示例 2：**

```
输入：arr = [1,-2,1], k = 5
输出：2
```

**示例 3：**

```
输入：arr = [-1,-2], k = 7
输出：0
```

**提示：**

- `1 <= arr.length <= 10^5`
- `1 <= k <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

### 解析

这里需要先给单一数组计算出四个值，分别是 `lmx`（从前向后最大子数组的和），`rmx`（从后向前最大子数组的和），`cmx`（整体的最大子数组的和），以及 `sum`（数组中所有元素的和）。

一共包括五种情况，分别是：

- `cmx`：一个数组的最大子数组的和。
- `sum * k`：`k` 个数组的和。
- `sum * (k - 1) + max(lmx, rmx)`：`k - 1` 个数组加上两侧中较大的子数组的和。
- `sum * (k - 2) + lmx + rmx`：`k - 2` 个数组加上两侧的子数组的和。
- `lmx + rmx`：两侧的子数组的和。

### 代码

```cpp
const int MOD = 1e9 + 7;

class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        int sum = 0, n = arr.size();
        for (auto v: arr) sum += v;
        
        int lmx = 0;  // 单个数组从前向后最大子数组的和
        for (int i = 0, cur = 0; i < n; i ++) {
            cur += arr[i];
            lmx = max(lmx, cur);
        }
        
        int rmx = 0;  // 单个数组从后向前最大子数组的和
        for (int i = n - 1, cur = 0; i >= 0; i --) {
            cur += arr[i];
            rmx = max(rmx, cur);
        }
        
        long long ans = 0;
        
        // 计算单个数组整体的最大子数组的和
        for (int i = 0, cur = 0; i < n; i ++) {
            cur += arr[i];
            cur = cur < 0 ? 0 : cur;
            ans = max(ans, 1LL * cur);
        }
        if (k == 1) {
            return ans % MOD;
        }
        
        ans = max(ans, 1LL * sum * k);
        ans = max(ans, 1LL * sum * (k - 1) + max(lmx, rmx));
        ans = max(ans, 1LL * sum * (k - 2) + lmx + rmx);
        ans = max(ans, 1LL * lmx + rmx);
        
        return ans % MOD;
    }
};
```