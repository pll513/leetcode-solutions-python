class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        numslen = len(nums)
        closestsum = sum(nums[:3])
        mindelta = abs(target - closestsum)
        for i in range(numslen - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, numslen - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                delta = target - threesum
                if delta == 0:
                    return threesum
                elif delta > 0:
                    if delta < mindelta:
                        mindelta = delta
                        closestsum = threesum
                    if nums[i] + 2 * nums[right] < target:
                        break
                    left += 1
                else:
                    if -delta < mindelta:
                        mindelta = -delta
                        closestsum = threesum
                    if nums[i] + 2 * nums[left] > target:
                        break
                    right -= 1
        return closestsum
