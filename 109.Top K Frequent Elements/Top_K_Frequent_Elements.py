class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [i[0] for i in collections.Counter(nums).most_common(k)]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.Counter(nums)
        nums = [(i, d[i]) for i in d]
        return [i[0] for i in sorted(nums, key=lambda x: -x[1])[:k]]
