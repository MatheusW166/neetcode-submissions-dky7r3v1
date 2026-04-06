class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for idx,n in enumerate(nums):
            complement = target - n

            if complement in mapping:
                break

            mapping[n] = idx

        return [mapping.get(complement),idx]
