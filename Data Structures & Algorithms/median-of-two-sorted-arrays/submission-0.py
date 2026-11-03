class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        totallen = len(merged)
        if totallen % 2 == 1:
            return merged[(totallen - 1) // 2]
        else: 
            return (merged[(totallen // 2)] + merged[((totallen - 1) // 2)]) / 2