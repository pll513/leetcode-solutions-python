class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        if len(nums) <= 1:
            return [nums]
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                continue
            hashmap[n] = n
            c = nums[:i] + nums[i + 1:]
            for l in self.permuteUnique(c):
                r.append([n] + l)
        return r
