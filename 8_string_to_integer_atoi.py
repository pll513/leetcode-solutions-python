class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        numstart = False
        numstr = ''
        negative = False

        for c in s:
            if numstart:
                if self.is_number(c):
                    numstr += c
                else:
                    break
            else:
                if self.is_number(c):
                    numstart = True
                    numstr += c
                elif c == '+':
                    numstart = True
                elif c == '-':
                    numstart = True
                    negative = True
                elif c == ' ':
                    continue
                else:
                    break

        if not numstr:
            return 0

        result = int(numstr)
        if negative:
            result = -result
        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN

        return result

    def is_number(self, c):
        return c >= '0' and c <= '9'