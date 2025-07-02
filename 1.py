class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = {}
        for i in range(len(nums)):
            if target - nums[i] in a:
                return[i,a[target - nums[i]]]
            a[nums[i]] = i