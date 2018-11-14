class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dcurr = dmax = step = 0
        for i, n in enumerate(nums):
            if dcurr < i:
                step += 1
                dcurr = dmax
            dmax = max(dmax, i + n)
        return step