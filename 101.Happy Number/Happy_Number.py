class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_sqart(num):
            sum = 0
            while num:
                val = num % 10
                sum += val * val
                num /= 10
            return sum

        slow = digit_sqart(n)
        fast = digit_sqart(n)
        fast = digit_sqart(fast)

        while slow != fast:
            slow = digit_sqart(slow)
            fast = digit_sqart(fast)
            fast = digit_sqart(fast)
        if slow == 1:
            return True
        else:
            return False
