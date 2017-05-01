class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        # """
        num_dic = {}
        for key, value in enumerate(nums):
            if value in num_dic and key - num_dic[value] <= k:
                return print(True)
            num_dic[value] = key
        return print(False)

        # num_dir = {}
        # flag = False
        # if len(nums) > 1:
        #     for key, value in enumerate(nums):
        #         if value not in num_dir:
        #             num_dir[value] = key
        #         else:
        #             if abs(num_dir[value] - key) <= k:
        #                 flag = True
        #             num_dir[value] = key
        # if flag:
        #     return print(True)
        # return print(False)

solution = Solution()
solution.containsNearbyDuplicate([1, 0, 1, 1], 1)