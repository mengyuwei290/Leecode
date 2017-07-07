class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                try:
                    if dic[i] != stack.pop():
                        return False
                except:
                    return False
        return not stack
