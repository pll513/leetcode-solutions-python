class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        r = 0
        negative = (dividend < 0) is not (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            d, sub = divisor, 1
            while d <= dividend:
                dividend -= d
                r += sub
                d <<= 1
                sub <<= 1
        if negative:
            r = -r
        return min(r, 2 ** 31 - 1)
