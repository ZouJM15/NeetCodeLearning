from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        places = defaultdict(list)
        for i in range(len(s)):
            places[s[i]].append(i)
        print(places)

# Example usage:
solution = Solution()
solution.characterReplacement("ACABABBA", 1)  # Output: 4