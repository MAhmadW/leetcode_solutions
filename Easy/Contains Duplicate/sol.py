class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_instances = {}
        for num in nums:
            num_instances[num] = 0
        for num in nums:
            num_instances[num] = num_instances[num] + 1
            if num_instances[num] > 1:
                return True
        return False
            