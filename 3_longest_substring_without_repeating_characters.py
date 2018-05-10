class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlst = ''
        maxlen = 0
        for c in s:
            index = strlst.find(c)
            if index != -1:
                strlst = strlst[index + 1:]
            strlst += c
            if len(strlst) > maxlen:
                maxlen = len(strlst)

        return maxlen