class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        length = len(s)
        num, stack, sign  = 0, [], '+'
        for i in range(length):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == length - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                else:
                    pass
                sign, num = s[i], 0
        return sum(stack)  
