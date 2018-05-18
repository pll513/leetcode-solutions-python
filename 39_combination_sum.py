class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        c, r = [[]], []
        while len(c) > 0:
            ctmp = []
            for l in c:
                llen = len(l)
                if llen > 0:
                    last = l[llen - 1]
                else:
                    last = -2 ** 31
                for n in candidates:
                    if n >= last:
                        cursum = sum(l) + n
                        if cursum < target:
                            ctmp.append(l + [n])
                        elif cursum == target:
                            r.append(l + [n])
                        else:
                            break
            c = ctmp
        return r
