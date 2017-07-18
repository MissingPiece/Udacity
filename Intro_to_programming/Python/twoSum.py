nums = [3,2,4]
target = 6
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            for index2, x in enumerate(nums):
                if i + x == target:
                    output = index, index2
                    return output
                else:
                    pass
