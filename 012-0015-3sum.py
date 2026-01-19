class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 二指针
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                twosum = nums[l]+nums[r]
                if twosum > -nums[i]:
                    r -= 1
                elif twosum < -nums[i]:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

# example usage: 三数之和
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]
