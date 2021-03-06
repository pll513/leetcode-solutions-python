class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        last = None
        for n in nums:
            if n != last:
                nums[cnt] = n
                cnt += 1
            last = n
        return cnt