class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}


        # nums=[2,5,5,11]
        # target=10
        """
        diff = {
            8: 0,
            5: 2,
            -1: 3
        }
        """

        for idx,n in enumerate(nums):
            complement = target - n
            
            if complement in mapping:
                break

            mapping[n] = idx

        return [mapping.get(complement),idx]
