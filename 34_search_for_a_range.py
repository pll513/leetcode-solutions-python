class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = [-1, -1]
        numslen = len(nums)
        start, end = 0, numslen - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                r = [mid, mid]
                i, j = 0, mid - 1
                while i <= j:
                    m = (i + j) // 2
                    if nums[m] != target:
                        if m < numslen - 1 and nums[m + 1] == target:
                            r[0] = m + 1
                            break
                        else:
                            i = m + 1
                    else:
                        if m == 0:
                            r[0] = 0
                            break
                        else:
                            j = m - 1
                i, j = mid + 1, numslen - 1
                while i <= j:
                    m = (i + j) // 2
                    if nums[m] != target:
                        if m > 1 and nums[m - 1] == target:
                            r[1] = m - 1
                            break
                        else:
                            j = m - 1
                    else:
                        if m == numslen - 1:
                            r[1] = numslen - 1
                            break
                        else:
                            i = m + 1
                break
        return r
