class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numslen = len(nums)
        if numslen > 1:
            for i in range(numslen - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    for j in range(numslen - 1, -1, -1):
                        if nums[j] > nums[i]:
                            nums[i], nums[j] = nums[j], nums[i]
                            # built-in sorted method is faster!!??
                            nums[i + 1:] = sorted(nums[i + 1:])
                            # start, end = i + 1, numslen - 1
                            # while start < end:
                            #     nums[start], nums[end] = nums[end], nums[start]
                            #     start += 1
                            #     end -= 1
                            return
            nums.sort()
