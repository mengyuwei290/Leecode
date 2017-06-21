class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, reminder = divmod(abs(numerator), abs(denominator))
        if numerator * denominator >= 0:
            sign = ''
        else:
            sign = '-'
        result = [sign + str(n), '.']
        stack = []

        while reminder not in stack:
            stack.append(reminder)
            frac, reminder = divmod(reminder * 10, abs(denominator))
            result.append(str(frac))

        idx = stack.index(reminder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
