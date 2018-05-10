class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negtive = False
        if x < 0:
            negtive = True
            x = -x

        result = 0
        while x > 0:
            remainder = x % 10
            result = result * 10 + remainder
            x = (x - remainder) // 10

        if negtive:
            result = -result
        if result > 2**31 - 1 or result < -2**31:
            result = 0

        return result