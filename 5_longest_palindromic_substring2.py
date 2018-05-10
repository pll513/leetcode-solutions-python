class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        left = 0
        right = 0
        slen = len(s)
        lens = [[0] * slen for i in range(slen)]

        for dist in range(slen):
            for x in range(slen - dist):
                y = x + dist
                if dist == 0:
                    lens[x][y] = 1
                elif dist == 1:
                    if s[x] == s[y]:
                        lens[x][y] = 2
                else:
                    if s[x] == s[y] and lens[x + 1][y - 1]:
                        lens[x][y] = lens[x + 1][y - 1] + 2
                if lens[x][y] > maxlen:
                    maxlen = lens[x][y]
                    left, right = x, y

        return s[left:right + 1]
