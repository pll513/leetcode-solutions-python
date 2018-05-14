class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = sorted(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            twosum = nums2[left] + nums2[right]
            if twosum < target:
                left += 1
            elif twosum > target:
                right -= 1
            else:
                index1 = nums.index(nums2[left])
                if nums2[left] == nums2[right]:
                    return sorted([index1, nums.index(nums2[right], index1 + 1)])
                else:
                    return sorted([index1, nums.index(nums2[right])])

        return None
