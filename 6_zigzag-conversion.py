class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        slen = len(s)
        cost = 2 * numRows - 2
        count = slen // cost
        remainder = slen % cost
        dist = numRows - 1

        if remainder <= numRows:
            numCols = count * dist + 1
        else:
            numCols = count * dist + 1 + remainder - numRows

        matrix = [[''] * numCols for i in range(numRows)]
        x = y = 0

        for i in range(slen):
            matrix[y][x] = s[i]
            if x % dist == 0:
                if y == 0:
                    up = False
                elif y == dist:
                    up = True
            if up:
                x += 1
                y -= 1
            else:
                y += 1

        return ''.join([''.join(raw) for raw in matrix])
