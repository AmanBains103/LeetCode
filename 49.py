class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        b = {}
        for i in range(len(strs)):
            a = list(strs[i])
            a.sort()
            c = "".join(a)
            if c in b:
                b[c].append(strs[i])
            else:
                b[c] = [strs[i]]
        return list(b.values())