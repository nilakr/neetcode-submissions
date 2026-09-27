class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            ordered = sorted(word)
            map[tuple(ordered)].append(word)
            #ordered = []
        return list(map.values())





