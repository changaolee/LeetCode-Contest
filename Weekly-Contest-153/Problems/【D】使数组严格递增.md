>  *题目原链接：[1187. 使数组严格递增](https://leetcode-cn.com/contest/weekly-contest-153/problems/make-array-strictly-increasing/)

### 题目

给你两个整数数组 `arr1` 和 `arr2`，返回使 `arr1` 严格递增所需要的最小「操作」数（可能为 0）。

每一步「操作」中，你可以分别从 `arr1` 和 `arr2` 中各选出一个索引，分别为 `i` 和 `j`，`0 <= i < arr1.length` 和 `0 <= j < arr2.length`，然后进行赋值运算 `arr1[i] = arr2[j]`。

如果无法让 `arr1` 严格递增，请返回 -1。

**示例 1：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
```

**示例 2：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
输出：2
解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
```

**示例 3：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
输出：-1
解释：无法使 arr1 严格递增。
```

**提示：**

- `1 <= arr1.length, arr2.length <= 2000`
- `0 <= arr1[i], arr2[i] <= 10^9`

### 解析
首先，我们在对 `arr1` 进行遍历时有两种选择，第一种是保留当前数字，这时需要保证后面的数字要大于当前数字；第二种是从 `arr2` 中选择一个比当前数字大的数字与当前数字交换，而且很容易看出，我们要从 `arr2` 中选择尽可能小的数字才能给后面留下更大的选择空间。

因此，这里使用一个二维的 `dp` 数字，`dp[i][j]` 表示保证前 `i` 个元素严格递增所需要的最小操作次数。另外，
- 当 `j < arr2.length` 时，表示将 `arr1[i]` 与 `arr2[j]` 进行交换所需的最小操作次数
- 当 `j == arr2.length` 时，表示保留 `arr1[i]` 所需的最小操作次数

最后，只需遍历 `dp[n - 1]` 即可找到使 `arr1` 严格单调递增所需的最小操作数。

### 代码
```cpp
class Solution {
    int dp[2050][2050];
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        vector<int> pool(arr2);
        sort(pool.begin(), pool.end());
        pool.erase(unique(pool.begin(), pool.end()), pool.end());
        
        int n = arr1.size(), m = pool.size();
        
        memset(dp, -1, sizeof(dp));
        dp[0][m] = 0;
        for (int i = 0; i < m; i ++) dp[0][i] = 1;
        
        for (int i = 0; i < n - 1; i ++) {
            for (int j = 0; j <= m; j ++) {
                if (dp[i][j] == -1) continue;
                int current_val = j == m ? arr1[i]: pool[j];
                
                //  不进行替换
                if (arr1[i + 1] > current_val) {
                    if (dp[i + 1][m] == -1 || dp[i + 1][m] > dp[i][j]) {
                        dp[i + 1][m] = dp[i][j];
                    }
                }
                
                // 找出最小的大于当前值的元素进行替换
                int index = upper_bound(pool.begin(), pool.end(), current_val) - pool.begin();
                if (index < m) {
                    if (dp[i + 1][index] == -1 || dp[i + 1][index] > dp[i][j] + 1) {
                        dp[i + 1][index] = dp[i][j] + 1;
                    }
                }
            }
        }
        
        int ans = -1;
        for (int i = 0; i <= m; i ++){
            if (dp[n - 1][i] == -1) continue;
            if (ans == -1 || ans > dp[n - 1][i]) {
                ans = dp[n - 1][i];
            }
        }
        
        return ans;
    }
};
```