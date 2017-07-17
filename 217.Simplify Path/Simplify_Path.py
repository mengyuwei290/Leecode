class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for i in path.split('/'):
            if i  == '..':
                if stack:
                    stack.pop()
            elif i and i != '.':
                stack.append(i)
        return '/'+'/'.join(stack)
