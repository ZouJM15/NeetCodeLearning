class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num-1) not in numset:
                length = 1
                while (num+length) in numset:
                    length += 1
                longest = max(length, longest)

        return longest

# Example usage:
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))