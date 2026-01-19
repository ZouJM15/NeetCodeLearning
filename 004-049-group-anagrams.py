from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        print(res)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # There are 26 letters in the English alphabet
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


# Example usage:
# sol1 = Solution1()
# print(sol1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

sol2 = Solution2()
print(sol2.groupAnagrams(["act","pots","tops","cat","stop","hat"]))