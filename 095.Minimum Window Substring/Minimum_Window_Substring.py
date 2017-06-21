class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)

        I = J = i = 0

        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1

            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if not J or J - I > j - i:
                    J, I = j, i
        return s[I:J]
