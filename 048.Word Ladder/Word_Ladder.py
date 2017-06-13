class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def dfs_search(begin, end, d, length):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, step = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return step
                    for i in range(length):
                        s = word[:i] + '_' + word[i + 1:]
                        neighbour = d.get(s, [])
                        for n in neighbour:
                            if n not in visited:
                                queue.append((n, step + 1))
            return 0

        d = construct_dict(wordList)
        return dfs_search(beginWord, endWord, d, len(beginWord))
