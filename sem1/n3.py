from enum import Enum


class Color(Enum):
    WHITE = 0,
    BLACK = 1,


def route_exists(adj_list: list[list[int]], v: int, u: int) -> bool:
    col = [Color.WHITE] * len(adj_list)

    def dfs_for_x(vert: int, x: int) -> bool:
        col[vert] = Color.BLACK
        if x in adj_list[vert]:
            return True
        for adj in adj_list[vert]:
            if (col[adj] == Color.WHITE) and dfs_for_x(adj, x):
                return True
        return False

    return dfs_for_x(v, u) and dfs_for_x(u, v)
