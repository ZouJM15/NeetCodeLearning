class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        mp = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                print(s[r], mp[s[r]])
                l = max(l, mp[s[r]] + 1)# l直接跳到重复字符的下一个位置
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abba"))  # Output: 2