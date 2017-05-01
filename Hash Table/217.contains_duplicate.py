class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dir = {}
        for num in nums:
            if num in num_dir:
                return True
            else:
                num_dir[num] = False
        return False
