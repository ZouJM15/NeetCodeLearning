class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t) or len(s) != len(t):
            return False

        # # Method 1: sorted方法
        # return (sorted(s) == sorted(t))

        # # method 2：get方法：Counting frequency of each character in both strings
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return (countS == countT)

        # method 3: set方法
        set_s = set(s)

        num_1 = {}
        num_2 = {}
        for i in set_s:
            num_1[i] = s.count(i)
            num_2[i] = t.count(i)

        return (num_1 == num_2)

# Example usage:
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))  # Output: True
