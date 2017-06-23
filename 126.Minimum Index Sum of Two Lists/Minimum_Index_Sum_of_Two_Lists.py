class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        Aindex = {u: i for i, u in enumerate(list1)}
        best, ans = float('inf'), []

        for j, v in enumerate(list2):
            i = Aindex.get(v, float('inf'))
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
