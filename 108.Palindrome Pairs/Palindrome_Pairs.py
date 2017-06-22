class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_dict = {}
        res = []
        for i, word in enumerate(words):
            word_dict[word] = i
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]

                if tmp1[::-1] in word_dict and word_dict[tmp1[::-1]] != i and tmp2[::-1] == tmp2:
                    res.append([i, word_dict[tmp1[::-1]]])
                if j != 0 and tmp2[::-1] in word_dict and word_dict[tmp2[::-1]] != i and tmp1[::-1] == tmp1:
                    res.append([word_dict[tmp2[::-1]], i])
        return res
