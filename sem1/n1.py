# Считаем что граф направленый и может иметь кратные рёбра, нумерация вершин с 0

def adj_list_to_adj_matrix(adj_l):
    n = len(adj_l)
    adj_m = [[0] * n for i in range(n)]
    for i in range(n):
        for j in adj_l[i]:
            adj_m[i][j] += 1
    return adj_m


def adj_list_to_edge_list(adj_l):
    edge_l = []
    for i in range(len(adj_l)):
        for j in adj_l[i]:
            edge_l.append((i, j))
    return edge_l


def adj_matrix_to_adj_list(adj_m):
    n = len(adj_m)
    adj_l = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            adj_l[i] += [j] * adj_m[i][j]
    return adj_l


def adj_matrix_to_edge_list(adj_m):
    n = len(adj_m)
    edge_l = []
    for i in range(n):
        for j in range(n):
            edge_l[i] += (i, j) * adj_m[i][j]
    return edge_l


def edge_list_to_adj_list(edge_l):
    n = sorted(edge_l)[-1][0] + 1
    adj_l = [[] for i in range(n)]
    for i, j in edge_l:
        adj_l[i].append(j)
    return adj_l


def edge_list_to_adj_matrix(edge_l):
    n = sorted(edge_l)[-1][0] + 1
    adj_m = [[0] * n for i in range(n)]
    for i, j in edge_l:
        adj_m[i][j] += 1
    return adj_m
