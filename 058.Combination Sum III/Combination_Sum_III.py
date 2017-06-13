class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k <= 0:
            return []
        res = []

        def combinationSum3_helper(idx, path, sums, k, n):
            if k <= 0:
                if sums == n:
                    res.append(path[:])
                return None

            for i in range(idx, 10):
                if i not in path and sums + i <= n and k - 1 >= 0:
                    path += i,
                    combinationSum3_helper(i + 1, path, sums + i, k - 1, n)
                    path.pop()
            return

        combinationSum3_helper(1, [], 0, k, n)
        return res
