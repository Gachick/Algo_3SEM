from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        visited = [False] * n

        def mark_visited(v: int):
            visited[v] = True
            for i in range(n):
                if (isConnected[v][i] and not visited[i]):
                    mark_visited(i)

        for i in range(n):
            if (visited[i]):
                continue
            else:
                provinces += 1
                mark_visited(i)

        return provinces
