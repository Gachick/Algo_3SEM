from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0

        times = [-1] * n
        times[headID] = 0

        mx = 0

        def getTime(i):
            if times[i] != -1:
                return times[i]
            man = manager[i]
            times[i] = getTime(man) + informTime[man]
            return times[i]

        for i in range(n):
            mx = max(mx, getTime(i))

        return mx
