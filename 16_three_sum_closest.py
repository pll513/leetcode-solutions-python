class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        threesum = sum(nums[:3])
        mindelta = abs(target - threesum)
        for i, n in enumerate(nums):
            print(mindelta)
            twosum = self.two_sum_range(nums[i + 1:], target - n, mindelta)
            if twosum:
                threesum = n + twosum
                mindelta = abs(threesum - target)
        return threesum

    def two_sum_range(self, nums, target, delta):
        left, right = 0, len(nums) - 1
        result = None
        while left < right:
            if delta == 0:
                break
            twosum = nums[left] + nums[right]
            if twosum > target - delta:
                left += 1
            elif twosum > target + delta:
                right -= 1
            else:
                d = abs(target - twosum)
                if d < delta:
                    result = twosum
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        return result


def two_sum_range(nums, target, delta):
    import pdb; pdb.set_trace()
    print('target: ' + str(target))
    print(nums)
    left, right = 0, len(nums) - 1
    result = None
    while left < right:
        if delta == 0:
            break
        twosum = nums[left] + nums[right]
        if twosum <= target - delta:
            left += 1
        elif twosum >= target + delta:
            right -= 1
        else:
            d = abs(target - twosum)
            if d < delta:
                result = twosum
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
    print('result: ' + str(result))
    return result

two_sum_range([0, 1, 2], 4, 3)
