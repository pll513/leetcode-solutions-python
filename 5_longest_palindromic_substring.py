class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        longest = ''
        slen = len(s)
        
        if slen:
            maxlen = 1
            longest = s[0]
        
        for curr in range(slen):
            if curr >= 1 and s[curr] == s[curr - 1]:
                currlen = 2
                left = curr - 2
                right = curr + 1
                while left >= 0 and right < slen and s[left] == s[right]:
                    currlen += 2
                    left -= 1
                    right += 1
                if currlen > maxlen:
                    maxlen = currlen
                    longest = s[left + 1:right]
            if curr >= 2 and s[curr] == s[curr - 2]:
                currlen = 3
                left = curr - 3
                right = curr + 1
                while left >= 0 and right < slen and s[left] == s[right]:
                    currlen += 2
                    left -= 1
                    right += 1
                if currlen > maxlen:
                    maxlen = currlen
                    longest = s[left + 1:right]
            
        return longest