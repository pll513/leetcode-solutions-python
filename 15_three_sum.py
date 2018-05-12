class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        nums.sort()
        numslen = len(nums)
        for i in range(numslen - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, numslen - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == 0:
                    r.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threesum < 0:
                    if nums[i] + 2 * nums[right] < 0:
                        break
                    left += 1
                else:
                    if nums[i] + 2 * nums[left] > 0:
                        break
                    right -= 1
        return r
