class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            k1 = (m + n) // 2
            k2 = k1 + 1
            min1 = self.find_kth_min(nums1, nums2, k1)
            min2 = self.find_kth_min(nums1, nums2, k2)
            return (min1 + min2) / 2
        else:
            k1 = (m + n) // 2 + 1
            return self.find_kth_min(nums1, nums2, k1)

    def find_kth_min(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        if m == 0:
            if n == 0:
                return float(0)
            return float(nums2[k - 1])
        if k == 1:
            return float(min(nums1[0], nums2[0]))
        len1 = k // 2
        len2 = k - len1
        if len1 > m:
            len1 = m
            len2 = k - m
        if nums1[len1 - 1] == nums2[len2 - 1]:
            return nums1[len1 - 1]
        elif nums1[len1 - 1] < nums2[len2 - 1]:
            return self.find_kth_min(nums1[len1:], nums2, k - len1)
        else:
            return self.find_kth_min(nums1, nums2[len2:], k - len2)
