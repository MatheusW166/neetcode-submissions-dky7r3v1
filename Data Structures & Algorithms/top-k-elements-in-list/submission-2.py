class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        qtts = [set() for i in range(len(nums) + 1)] 

        for n in nums:
            counts[n] = counts.get(n,0) + 1

        for n,qtt in counts.items():                
            qtts[qtt].add(n)

        res = []
        for i in range(len(qtts) - 1,0,-1):
            for q in qtts[i]:
                res.append(q)
                if len(res) == k:
                    break
            else:
                continue
            break

        return res