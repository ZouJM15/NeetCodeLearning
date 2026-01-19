class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False 
    
# Example usage:
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True