def topological_sort(graph: list[list[int]]):
    visit = [False] * len(graph)
    queue = list(range(len(graph)))
    order = []

    while (len(queue) != 0):
        current = queue[0]
        if (visit[current]):
            queue.pop(0)
            continue
        if (all(map(lambda x: visit[x], graph[current]))):
            visit[current] = True
            order.insert(0, queue.pop(0))
        else:
            queue = graph[current] + queue

    return order
