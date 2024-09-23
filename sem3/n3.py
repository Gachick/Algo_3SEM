from typing import List


def transpose_graph(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    new_adj = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            new_adj[j].append(i)
    return new_adj


def topo_sort(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs(vert: int):
        visited[vert] = True
        for adj in graph[vert]:
            if not visited[adj]:
                dfs(adj)
        order.append(vert)

    for vert in range(n):
        if not visited[vert]:
            dfs(vert)

    return order[::-1]


def strong_components(graph: List[List[int]]) -> List[int]:
    t = transpose_graph(graph)
    topo_sorted = topo_sort(graph)
    n = len(graph)

    component_index = [-1] * n
    current_comp = 0

    def dfs(vert: int):
        component_index[vert] = current_comp
        for adj in t[vert]:
            if component_index[adj] == -1:
                dfs(adj)

    for vert in topo_sorted:
        if component_index[vert] == -1:
            dfs(vert)
            current_comp += 1

    return component_index


def component_graph(graph, comp_ind):
    comp_n = max(comp_ind)
    comp_adj = [[] for _ in range(comp_n)]

    for vert in range(len(graph)):
        cur_comp = comp_ind[vert]
        for adj in graph[vert]:
            adj_comp = comp_ind[adj]
            if adj_comp != cur_comp and adj_comp not in comp_adj[cur_comp]:
                comp_adj[cur_comp].append(adj_comp)

    return comp_adj


def min_added_edges(comp_graph):
    # считаем что граф компонент несвязный
    n = len(comp_graph)
    s = 0  # вершины источники
    t = 0  # вершины стоки
    q = 0  # вершины изолированные
    edge_starts = []
    edge_ends = []
    for i in range(n):
        for adj in comp_graph[i]:
            edge_starts.append(i)
            edge_ends.append(adj)
    for i in range(n):
        if i in edge_starts:
            s += 1
        elif i in edge_ends:
            t += 1
        else:
            q += 1
    return max(q+s, q+t)
