class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        charmap = [
            None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv',
            'wxyz'
        ]
        r = list(charmap[int(digits[0])])
        for digit in digits[1:]:
            rtmp = []
            for s in r:
                for c in charmap[int(digit)]:
                    rtmp.append(s + c)
            r = rtmp
        return r
