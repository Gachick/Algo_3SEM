from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_l = [[] for i in range(n)]
        for conn in connections:
            adj_l[conn[0]].append(conn[1])
            adj_l[conn[1]].append(conn[0])

        times = [-1] * n
        critical = []

        def dfs(vert, time, previous):
            times[vert] = time + 1
            min_time = time + 1
            for adj in adj_l[vert]:
                if adj == previous:
                    continue
                if times[adj] == -1:
                    dfs(adj, time + 1, vert)
                min_time = min(min_time, times[adj])
                if times[adj] > time + 1:
                    critical.append([vert, adj])
            times[vert] = min_time

        dfs(0, 0, -1)

        return critical


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(Solution().criticalConnections(n, connections))
n = 2
connections = [[0, 1]]
print(Solution().criticalConnections(n, connections))
