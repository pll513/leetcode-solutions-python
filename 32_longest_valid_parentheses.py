class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = start = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                elif len(stack) == 1:
                    stack.pop()
                    ans = max(ans, i - start + 1)
                else:
                    stack.pop()
                    ans = max(ans, i - stack[-1])
        return ans
