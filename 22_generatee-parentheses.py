class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        r = ['(']
        left = [n - 1]
        right = [n]
        for cnt in range(2 * n - 1):
            rtmp, lefttmp, righttmp = [], [], []
            for i, s in enumerate(r):
                if left[i]:
                    rtmp.append(s + '(')
                    lefttmp.append(left[i] - 1)
                    righttmp.append(right[i])
                if right[i] > left[i]:
                    rtmp.append(s + ')')
                    lefttmp.append(left[i])
                    righttmp.append(right[i] - 1)
            r, left, right = rtmp, lefttmp, righttmp
        return r