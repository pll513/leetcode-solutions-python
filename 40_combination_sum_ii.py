class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        c, d, r = [sorted(candidates)], [[]], []
        while c:
            ctmp, dtmp = [], []
            for i, l in enumerate(d):
                suml = sum(l)
                last = -1
                for j, n in enumerate(c[i]):
                    if n == last:
                        continue
                    else:
                        last = n
                        cursum = suml + n
                        if cursum < target:
                            ctmp.append(c[i][j+1:])
                            dtmp.append(l + [n])
                        elif cursum == target:
                            r.append(l + [n])
                        else:
                            break
            c, d = ctmp, dtmp
        return r
