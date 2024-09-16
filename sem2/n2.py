def topological_sort(graph: list[list[int]]):
    visit = [False] * len(graph)
    order = []

    def dfs(vertex: int):
        visit[vertex] = True
        for u in graph[vertex]:
            if not visit[u]:
                dfs(u)

        order.append(vertex)

    for vertex in range(len(graph)):
        if not visit[vertex]:
            dfs(vertex)

    return order[::-1]


vertices = [
    "Пиджак",
    "Часы",
    "Брюки",
    "Рубашка",
    "Трусы",
    "Носки",
    "Туфли",
    "Галстук",
    "Ремень"
]

adj_list = [[], [], [6, 8], [8, 7], [2, 6], [6], [], [0], [0]]

print(*map(lambda x: vertices[x], topological_sort(adj_list)))
