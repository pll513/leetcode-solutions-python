class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen, plen = len(s), len(p)
        r = [[False] * (plen + 1) for i in range(slen + 1)]
        r[0][0] = True
        for i in range(1, slen):
            r[i][0] = False
        for j in range(plen):
            r[0][j+1] = r[0][j] and p[j] == '*'
        for i in range(slen):
            for j in range(plen):
                if p[j] == '?':
                    r[i+1][j+1] = r[i][j]
                elif p[j] == '*':
                    r[i+1][j+1] = r[i][j] or r[i][j+1] or r[i+1][j]
                else:
                    r[i+1][j+1] = r[i][j] and s[i] == p[j]
        return r[slen][plen]
