class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numslen = len(nums)
        for i in range(numslen):
            while i + 1 != nums[i] and nums[i] > 0 and nums[i] <= numslen and nums[nums[i] - 1] != nums[i]:
                n = nums[i]
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
        for i in range(numslen):
            if i + 1 != nums[i]:
                return i + 1
        return numslen + 1
