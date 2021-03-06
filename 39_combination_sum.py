class Solution:
    def combinationSum(self, candidates, target):
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
                if l:
                    smallest = l[-1]
                else:
                    smallest = -2**32
                for j, n in enumerate(c[i]):
                    if n >= smallest:
                        cursum = suml + n
                        if cursum < target:
                            ctmp.append(c[i])
                            dtmp.append(l + [n])
                        elif cursum == target:
                            r.append(l + [n])
                        else:
                            break
            c, d = ctmp, dtmp
        return r
