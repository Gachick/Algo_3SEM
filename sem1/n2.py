from enum import Enum


class Color(Enum):
    WHITE = 0,
    BLACK = 1,
    GRAY = 2


def find_cycle_dir(adj_list: list[list[int]]) -> bool:
    col = [Color.WHITE] * len(adj_list)

    def dfs_odd(vert: int) -> bool:
        if (vert % 2 == 0):
            col[vert] = Color.BLACK
            return False

        col[vert] = Color.GRAY
        for adj in adj_list[vert]:
            if col[adj] == Color.GRAY or (col[adj] == Color.WHITE and dfs_odd(adj)):
                return True
        col[vert] = Color.BLACK
        return False

    for vert in range(len(adj_list)):
        if col[vert] == Color.WHITE and dfs_odd(vert):
            return True
    return False
