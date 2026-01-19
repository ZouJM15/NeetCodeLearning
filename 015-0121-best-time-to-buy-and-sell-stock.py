class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 滑动窗口
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

        # # 双指针
        # l, r = 0, 1
        # res = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         res = max(res, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return res

# Example usage:
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([7,6,4,3,1]))    # Output: 0

