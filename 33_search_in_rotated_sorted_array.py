class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                if nums[mid] <= nums[end]:
                    i, j = mid + 1, end
                    while i <= j:
                        m = (i + j) // 2
                        if nums[m] < target:
                            i = m + 1
                        elif nums[m] > target:
                            j = m - 1
                        else:
                            return m
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                if nums[mid] >= nums[start]:
                    i, j = start, mid - 1
                    while i <= j:
                        m = (i + j) // 2
                        if nums[m] < target:
                            i = m + 1
                        elif nums[m] > target:
                            j = m - 1
                        else:
                            return m
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return mid
        return -1
