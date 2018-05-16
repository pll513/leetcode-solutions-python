class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        for i in range(len(haystack) - nlen + 1):
            if haystack[i:i + nlen] == needle:
                return i
        return -1
