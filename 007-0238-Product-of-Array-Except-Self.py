# a = [1,2,3,4]
# n = len(a)
# for i in range(1, n):# i左侧的乘积
#     print(i, a[i])
# for i in range(n - 2, -1, -1):# i右侧的乘积
#     print(i, a[i])

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pro = [1] * n
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            pro[i] = left[i] * right[i]
        return pro
    
# Example usage:
sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))
