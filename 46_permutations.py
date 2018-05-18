class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numslen = len(nums)
        if numslen < 1:
            return [[]]
        r, c = [[]], [nums]
        for i in range(numslen):
            rtmp, ctmp = [], []
            for i, per in enumerate(r):
                for j, n in enumerate(c[i]):
                    rtmp.append(per + [n])
                    ctmp.append(c[i][:j] + c[i][j + 1:])
            r, c = rtmp, ctmp
        return r
