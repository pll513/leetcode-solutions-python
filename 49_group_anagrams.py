class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in hashmap:
                hashmap[ss].append(s)
            else:
                hashmap[ss] = [s]
        return [hashmap[key] for key in hashmap]
