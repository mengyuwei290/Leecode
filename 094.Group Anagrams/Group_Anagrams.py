class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        if len(strs) == 1 and not strs[0]:
            return [[""]]

        d = {}
        for s in strs:
            s_t = ''.join(sorted(list(s)))
            d[s_t] = d.get(s_t, []) + [s]

        res = []
        for v in d.values():
            res.append(v)
        return res
