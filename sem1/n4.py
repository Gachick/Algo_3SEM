class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        judje_candidates = {i + 1: 0 for i in range(n)}
        for i, j in trust:
            if i in judje_candidates:
                judje_candidates.pop(i)
            if j in judje_candidates:
                judje_candidates[j] += 1
        for i in judje_candidates:
            if judje_candidates[i] == n - 1:
                return i
        return -1
