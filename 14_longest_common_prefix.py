class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            prefix = prefix[:len(s)]
            for i in range(len(prefix)):
                if prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break

        return prefix
