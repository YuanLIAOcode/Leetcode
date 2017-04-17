
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = {}
    for i in range(len(nums)):
        if nums[i] not in result:
            result[target - nums[i]] = i
        else:
            return [result[nums[i]], i]


nums = [2, 6, 4, 1, 7]
target = 9
print(twoSum(nums, target))