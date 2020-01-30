> *题目原链接：[1200. 最小绝对差](https://leetcode-cn.com/contest/weekly-contest-155/problems/minimum-absolute-difference)*

### 题目

给你个整数数组 `arr`，其中每个元素都 **不相同** 。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

**示例 1：**

``` 
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
```    

**示例 2：**

```
输入：arr = [1,3,6,10,15]
输出：[[1,3]]
```

**示例 3：**

```
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
```

**提示：**

* `2 <= arr.length <= 10^5`
* `-10^6 <= arr[i] <= 10^6`

### 解析

先排序，然后在遍历过程中维护当前已知最小差值的元素对列表。
    
### 代码

```cpp
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        
        vector<vector<int>> ans;
        int minDistance = INT_MAX;
        for (int i = 1; i < arr.size(); i ++) {
            if (arr[i] - arr[i - 1] < minDistance) {
                ans.clear();
                ans.push_back(vector<int>{arr[i - 1], arr[i]});
                minDistance = arr[i] - arr[i - 1];
            } else if (arr[i] - arr[i - 1] == minDistance) {
                ans.push_back(vector<int>{arr[i - 1], arr[i]});
            }
        }
        return ans;
    }
};
```