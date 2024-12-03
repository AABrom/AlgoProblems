class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        # values of dict = indices of num
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i