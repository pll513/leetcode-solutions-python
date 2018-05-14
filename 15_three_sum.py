class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        nums2 = sorted(nums)
        for i, n in enumerate(nums2):
            if n > 0:
                break
            if i > 0 and n == nums2[i - 1]:
                continue
            for pair in self.two_sum(nums2[i + 1:], -n):
                group = sorted(pair + [n])
                lst.append(group)

        return lst

    def two_sum(self, nums, target):
        lst = []
        left, right = 0, len(nums) - 1
        while left < right:
            twosum = nums[left] + nums[right]
            if twosum < target:
                left += 1
            elif twosum > target:
                right -= 1
            else:
                lst.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        return lst
