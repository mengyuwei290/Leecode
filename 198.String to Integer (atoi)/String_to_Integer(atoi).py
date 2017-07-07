class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            str = str.lstrip() + '$' # remove leading spaces and append an end mark
            for i, ch in enumerate(str):
                if not (ch in '+-' or '0' <= ch <= '9'):
                    result = int(str[:i])
                    return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
        except:
            return 0
