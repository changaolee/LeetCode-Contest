> *题目原链接：[1184. 公交站间的距离](https://leetcode-cn.com/contest/weekly-contest-153/problems/distance-between-bus-stops/)*

### 题目

环形公交路线上有 `n` 个站，按次序从 `0` 到 `n - 1` 进行编号。我们已知每一对相邻公交站之间的距离，`distance[i]` 表示编号为 `i` 的车站和编号为 `(i + 1) % n` 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 `start` 到目的地 `destination` 之间的最短距离。

**示例 1：**

```
输入：distance = [1,2,3,4], start = 0, destination = 1
输出：1
解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。
```

**示例 2：**

```
输入：distance = [1,2,3,4], start = 0, destination = 2
输出：3
解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
```

**示例 3：**

```
输入：distance = [1,2,3,4], start = 0, destination = 3
输出：4
解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。
```

**提示：**

- `1 <= n <= 10^4`
- `distance.length == n`
- `0 <= start, destination < n`
- `0 <= distance[i] <= 10^4`

### 解析

首先，由于公交路线是环形的，乘客从出发点 `start` 到目的地 `destination` 只有两种方式：逆时针和顺时针。

因此，只需比较这两个距离的长短即可。注意：逆时针距离可通过总距离减去顺时针的距离。

### 代码

```cpp
class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int sum = 0, ret = 0;
        for (int i = 0; i < distance.size(); ++ i) {
            sum += distance[i];
        }
        while (start != destination) {
            ret += distance[start];
            start = (start + 1) % distance.size();
        }
        return min(ret, sum - ret);
    }
};
```