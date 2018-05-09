class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        dnums = {}
        for i in range(len_nums):
            num = nums[i]
            num2 = target - num
            if num2 in dnums:
                return sorted([i, dnums[num2]])
            dnums[num] = i
        return None