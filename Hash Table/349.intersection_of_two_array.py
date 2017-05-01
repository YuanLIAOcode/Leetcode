class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)


num1 = [1,2,2,3,4,2,5,8,9,1,10]
num2 = [2,3,4,2,5,6,8]
solution = Solution()
print(solution.intersection(num1, num2))
