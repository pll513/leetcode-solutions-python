class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        xx = x
        y = 0

        while xx > 0:
            remainder = xx % 10
            xx = (xx - remainder) // 10
            y = y * 10 + remainder

        return x == y and x <= 2**31 - 1
