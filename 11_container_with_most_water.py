class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxarea = 0

        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                if area > maxarea:
                    maxarea = area
                left += 1
            else:
                area = (right - left) * height[right]
                if area > maxarea:
                    maxarea = area
                right -= 1

        return maxarea
