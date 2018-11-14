class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = {}
        r = []
        wordcnt = len(words)
        if wordcnt == 0:
            return []
        wordlen = len(words[0])
        wordlentotal = wordlen * wordcnt
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        for i in range(len(s) - wordlentotal + 1):
            dc = d.copy()
            flag = True
            for j in range(i, i + wordlentotal, wordlen):
                ss = s[j:j + wordlen]
                if ss in dc and dc[ss] > 0:
                    dc[ss] -= 1
                else:
                    flag = False
                    break
            if flag:
                r.append(i)
        return r


Solution().findSubstring('caaacaaabbbaaabbb', ['aaa', 'bbb', 'aaa'])
