class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口 s长t短
        # r 先移动，等到扫描到t的最后一个字符，就移动l，直到窗口中
        if t=="":
            return ""

        countT = {} # 记录t中字符及其数量
        for c in t:
            countT[c] = countT.get(c,0) + 1
        window = {} # sliding window，记录字符及其出现次数
        have = 0
        need = len(countT)

        l = 0
        for r in range(len(s)):
            c = s[r]
            # 移动right，将s中的字符存入window
            window[c] = window.get(c, 0) + 1 

            if c in countT and window[c] == countT[c]:
                have += 1

            # 当扫描到s[r]时，t中的字符种类与windows相应字符一致（不考虑数量），移动left
            # t中的字符种类与windows相应字符一致如何表示？就是上面那个if的表示
            while have == need: # 已确定r的位置
                # 移动window中left，若删除的该字符是t中的且移动后数量小于t，则说明已移动到窗口最小位
                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return s[l : r + 1]   

# example usage:
solution = Solution()
print(solution.minWindow("OUYDYXAZVXYZ", "XYZ"))  # Expected output: "BANC"