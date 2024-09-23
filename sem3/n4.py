from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        from enum import Enum

        class Color(Enum):
            White = 0,
            Black = 1,
            Grey = 2

        n = len(colors)
        adj_l = [[] for i in range(n)]
        adj_l_inversed = [[] for i in range(n)]
        for edge in edges:
            adj_l_inversed[edge[1]].append(edge[0])
            adj_l[edge[0]].append(edge[1])

        color = [Color.White] * n
        heads = []
        cycles = False

        def topo(vert):
            color[vert] = Color.Grey
            if len(adj_l_inversed[vert]) == 0:
                heads.append(vert)
            for adj in adj_l_inversed[vert]:
                if color[adj] == Color.Grey:
                    nonlocal cycles
                    cycles = True
                if color[adj] == Color.White:
                    topo(adj)
            color[vert] = Color.Black
        for vert in range(n):
            if color[vert] == Color.White:
                topo(vert)
        if cycles:
            return -1

        mx = -1
        cache = []

        def dfs(vert, char):
            if cache[vert] != -1:
                return cache[vert]
            count = 0
            for adj in adj_l[vert]:
                count = max(count, dfs(adj, char))
            if char == colors[vert]:
                count += 1
            cache[vert] = count
            return count
        for head in heads:
            for char in set(colors):
                cache = [-1] * n
                mx = max(mx, dfs(head, char))

        return mx
