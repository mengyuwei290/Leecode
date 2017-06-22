class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ds = collections.Counter(s)
        ls = len(ds)

        return "".join([i[0] * i[1] for i in ds.most_common(ls)])
