class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen = len(s)
        plen = len(p)
        r = [[False] * (plen + 1) for i in range(slen + 1)]
        r[0][0] = True
        for j in range(1, plen, 2):
            r[0][j + 1] = r[0][j - 1] and p[j] == '*'
        if slen < 1 or plen < 1:
            return r[slen][plen]
        r[1][1] = s[0] == p[0] or p[0] == '.'
        for i in range(0, slen):
            for j in range(1, plen):
                if p[j] == '*':
                    r[i + 1][j + 1] = r[i + 1][j - 1] or r[i + 1][j] or r[i][j +
                                                                             1] and (s[i] == p[j - 1] or p[j - 1] == '.')
                else:
                    r[i + 1][j + 1] = r[i][j] and (s[i] == p[j] or p[j] == '.')
        return r[slen][plen]
