class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 双指针做法
        l = 0
        r = len(numbers) - 1
        while l < r:
            n1n2sum = numbers[l] + numbers[r]
            if n1n2sum > target:
                r -= 1
            elif n1n2sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []

# Example usage:有序数组的两数之和
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # [1, 2]
