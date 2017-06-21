class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        n, cnt = len(s), len(words)
        if n <= 0 or cnt <= 0:
            return []

        dt = dict()
        for word in words:
            dt[word] = dt.get(word, 0) + 1

        wl = len(words[0])

        for i in range(wl):
            left, count = i, 0
            dt_temp = dict()
            for j in range(i, n, wl):
                str1 = s[j:j + wl]
                if str1 in dt:  # is a vaild substring
                    dt_temp[str1] = dt_temp.get(str1, 0) + 1
                    if dt_temp[str1] <= dt[str1]:
                        count += 1
                    else:
                        while dt_temp[str1] > dt[str1]:
                            str_temp = s[left:left + wl]
                            dt_temp[str_temp] -= 1
                            if dt_temp[str_temp] < dt[str_temp]:
                                count -= 1
                            left += wl
                    if count == cnt:
                        res.append(left)
                        dt_temp[s[left:left + wl]] -= 1
                        count -= 1
                        left += wl
                else:  # is not a valie substring
                    count, left = 0, j + wl
                    dt_temp.clear()
        return res
