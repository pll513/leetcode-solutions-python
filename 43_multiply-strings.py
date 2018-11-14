class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2 or num1 == '0' or num2 == '0':
            return '0'
        rnum1 = num1[::-1]
        zeros = ''
        r = ''
        for n2 in num2[::-1]:
            product = ''
            carry = 0
            for n1 in rnum1:
                sum = carry + int(n1) * int(n2)
                carry = sum // 10
                product = str(sum % 10) + product
            if carry:
                product = str(carry) + product
            r = addtwo(r, product + zeros)
            zeros += '0'
        return r


def addtwo(a, b):
    len1 = len(a)
    carry = 0
    r = ''
    for i in range(len(b)):
        if len1 - i - 1 >= 0:
            sum = carry + int(a[-i - 1]) + int(b[-i - 1])
        else:
            sum = carry + int(b[-i - 1])
        carry = sum // 10
        r = str(sum % 10) + r
    if carry:
        r = '1' + r
    return r
