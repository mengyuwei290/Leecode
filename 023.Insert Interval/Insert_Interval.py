# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right, newstart, newend = [], [], newInterval.start, newInterval.end
        for i in intervals:
            if i.end < newInterval.start:
                left += i,
            elif i.start > newInterval.end:
                right += i,
            else:
                newstart = min(newstart, i.start)
                newend = max(newend, i.end)
        newInterval.start, newInterval.end = newstart, newend
        return left + [newInterval] + right
