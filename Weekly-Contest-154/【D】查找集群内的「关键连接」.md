> *题目原链接：[1192. 查找集群内的「关键连接」](https://leetcode-cn.com/contest/weekly-contest-154/problems/critical-connections-in-a-network/)*

### 题目

力扣数据中心有 `n` 台服务器，分别按从 `0` 到 `n-1` 的方式进行了编号。

它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 `connections` 是无向的。

从形式上讲，`connections[i] = [a, b]` 表示服务器 `a` 和 `b` 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。

「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。

请你以任意顺序返回该集群内的所有 「关键连接」。

**示例 1：**

![image](./Resources/critical-connections-in-a-network.png)

```
输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
输出：[[1,3]]
解释：[[3,1]] 也是正确的。
```

**提示：**

- `1 <= n <= 10^5`
- `n-1 <= connections.length <= 10^5`
- `connections[i][0] != connections[i][1]`
- 不存在重复的连接

### 解析

使用 Tarjan算法：求解图的割点与桥（割边）[参考链接](https://www.cnblogs.com/nullzx/p/7968110.html)

### 代码

```cpp
class Solution {
public:
    vector<vector<int>> res;
    int index = 0;
    vector<int> dfn;
    vector<int> low;
    vector<vector<int>> graph;
    
    void tarjan(int cur, int parent)
    {
        low[cur] = dfn[cur] = index ++;
        for (const auto& next : graph[cur]) {
            if(next == parent) continue;  // 由题可知：不存在重复的连接，避免重复访问
            if (dfn[next] == -1) {  // 没有访问过，继续 DFS
                tarjan(next, cur);
                low[cur] = min(low[cur], low[next]);  // 更新能访问的最小序号的祖先结点
                if(low[next] > dfn[cur]) {  // 新的节点的 low 已经大于当前节点的序号，说明已经不在同一个强联通分量里了
                    res.push_back({cur, next});
                }
            } else {  // 已访问过结点，则回溯与祖先结点的 dfn 值对比，更新 low 值
                low[cur] = min(low[cur], dfn[next]);
            }
        }
    }

    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        dfn.resize(n, -1);
        low.resize(n, -1);    
        graph.resize(n);
        for (int i = 0; i < connections.size(); i++) {
            vector<int>& c = connections[i];
            graph[c[0]].push_back(c[1]);
            graph[c[1]].push_back(c[0]);
        }
        tarjan(0, -1);
        return res;
    }
};
```