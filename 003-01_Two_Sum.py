class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[n] = i
        return []

# Example usage:
sol = Solution()
print(sol.twoSum([4,5,6], 10))  # Output: 