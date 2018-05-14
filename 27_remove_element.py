class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        for n in nums:
            if n != val:
                n, nums[cnt] = nums[cnt], n
                cnt += 1
        return cnt