class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        i = 1
        while i < len(nums):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
            i += 1
        return print(major)

solution = Solution()
solution.majorityElement([3,3,4])