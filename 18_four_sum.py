class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = []
        nums.sort()
        numslen = len(nums)
        for i in range(numslen - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, numslen - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                left, right = j + 1, numslen - 1
                while left < right:
                    foursum = nums[i] + nums[j] + nums[left] + nums[right]
                    if foursum == target:
                        r.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif foursum < target:
                        if nums[i] + nums[j] + 2 * nums[right] < target:
                            break
                        left += 1
                    else:
                        if nums[i] + nums[j] + 2 * nums[left] > target:
                            break
                        right -= 1
        return r
