from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1 #{1: 3, 2: 2, 3: 1, 4: 1}
        # 按value降序排序，得到排序后的元组列表
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)# 输出：[(1, 3), (2, 2), (3, 1), (4, 1)]
        return [key for key, value in sorted_hashmap[:k]]

# Example usage:
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,4], 2))