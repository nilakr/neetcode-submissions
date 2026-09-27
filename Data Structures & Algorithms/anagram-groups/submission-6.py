class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map = defaultdict(list)
        # letterList = [0]*26
        # for word in strs:
        #     for letter in word:
        #         letterList[ord(letter) - ord('a')]+=1
        #     map[tuple(letterList)].append(word)
        #     letterList = [0]*26
        
        # return list(map.values())

        map = defaultdict(list)
        for word in strs:
            ordered = "".join(sorted(word))
            map[ordered].append(word)
            ordered = []
        return list(map.values())





