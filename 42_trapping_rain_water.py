class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxpos = 0
        maxheight = 0
        r = 0
        for i, h in enumerate(height):
            if h > maxheight:
                maxpos, maxheight = i, h
        maxh = 0
        for i in range(maxpos):
            if height[i] < maxh:
                r += maxh - height[i]
            else:
                maxh = height[i]
        maxh = 0
        for i in range(len(height)-1, maxpos, -1):
            if height[i] < maxh:
                r += maxh - height[i]
            else:
                maxh = height[i]
        return r
