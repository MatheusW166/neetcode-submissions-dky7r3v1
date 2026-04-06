from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for _,qtt in counts.items():
            if qtt>1:
                return True
        return False