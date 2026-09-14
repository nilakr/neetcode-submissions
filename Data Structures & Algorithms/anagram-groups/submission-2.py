class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        """for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')]+=1"""
        for word in strs:
            mapping[tuple(sorted(word))].append(word)
        return list(mapping.values())



