>  *题目原链接：[1186. 删除一次得到子数组最大和](https://leetcode-cn.com/contest/weekly-contest-153/problems/maximum-subarray-sum-with-one-deletion/)*

### 题目

给你一个整数数组，返回它的某个 **非空** 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。

换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 **不能为空**。

**示例 1：**

```
输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
```

**示例 2：**

```
输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。
```

**示例 3：**

```
输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
```

**提示：**

- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

### 解析

假如我们已经选取了一段连续数组 `[l...r]`，并从中间删去了一个数 `mid`，那么我们的数组就变成了 `[l...mid)` 和 `(mid...r]`。也就是说，我们如果确定删去 `mid` 的话，还需要知道 `mid` 左边的最大连续子段和和 `mid` 右边的最大连续子段和。换句话说，需要知道 `mid - 1` 为结尾的最大连续子段和以及以 `mid + 1` 为开头的最大连续子段和。

因此，我们需要使用两个辅助数组分别记录以每个数为结尾和开头的最大连续子段和，最后枚举要删除的数求值取 `max` 就可以了。

### 代码

```cpp
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        const int n = arr.size();
        
        if (n == 1) {
            return arr[0];
        }
        
        if (*max_element(arr.begin(), arr.end()) < 0) {
            return *max_element(arr.begin(), arr.end());
        }
        
        vector<int> left(n, 0), right(n, 0);
        
        left[0] = max(0, arr[0]);
        for (int i = 1; i < n; ++i) {  // 以 i 为结尾的最大子段和
            left[i] = max(0, left[i - 1] + arr[i]);
        }
        right[n - 1] = max(0, arr[n - 1]);
        for (int i = n - 2; i >= 0; --i) {  // 以 i 为开头的最大子段和
            right[i] = max(0, right[i + 1] + arr[i]);
        }
        
        int ans = 0;
        for (int i = 1; i < n - 1; i ++) {
            ans = max(ans, left[i - 1] + right[i + 1] + max(0, arr[i]));
        }
        ans = max(ans, right[1] + max(0, arr[0]));
        ans = max(ans, left[n - 2] + max(0, arr[n - 1]));
        
        return ans;
    }
};
```