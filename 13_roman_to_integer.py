class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == 'M':
                num += 1000
            elif c == 'D':
                num += 500
            elif c == 'L':
                num += 50
            elif c == 'V':
                num += 5
            elif c == 'C':
                if i + 1 < len(s) and s[i + 1] == 'D':
                    num += 400
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'M':
                    num += 900
                    i += 1
                else:
                    num += 100
            elif c == 'X':
                if i + 1 < len(s) and s[i + 1] == 'L':
                    num += 40
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'C':
                    num += 90
                    i += 1
                else:
                    num += 10
            elif c == 'I':
                if i + 1 < len(s) and s[i + 1] == 'V':
                    num += 4
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'X':
                    num += 9
                    i += 1
                else:
                    num += 1
            i += 1
                    
        return num