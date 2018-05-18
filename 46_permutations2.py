class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        if len(nums) <= 1:
            return [nums]
        for i, n in enumerate(nums):
            c = nums[:i] + nums[i + 1:]
            for l in self.permute(c):
                r.append([n] + l)
        return r
