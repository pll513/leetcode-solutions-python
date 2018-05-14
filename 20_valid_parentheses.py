class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False
            elif c == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != '[':
                    return False
            elif c == '}':
                if len(stack) == 0:
                    return False
                if stack.pop() != '{':
                    return False
        if len(stack):
            return False
        return True
