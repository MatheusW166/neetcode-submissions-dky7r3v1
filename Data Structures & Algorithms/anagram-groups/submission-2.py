from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = dict()

        for word in strs:
            # Using frozenset, so we're 
            # able to use as dict key
            key = frozenset(Counter(word).items())

            prev_group = anagrams_map.get(key,[])
            anagrams_map[key] = [word,*prev_group]
        
        return list(anagrams_map.values())
