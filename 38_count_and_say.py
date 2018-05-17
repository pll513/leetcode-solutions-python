class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2:
            return '1'
        s = '1'
        for i in range(1, n):
            cs = ''
            cnt = 0
            target = s[0]
            for c in s:
                if c == target:
                    cnt += 1
                else:
                    cs += str(cnt) + str(target)
                    target = c
                    cnt = 1
            cs += str(cnt) + str(target)
            s = cs
        return s
