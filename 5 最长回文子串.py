"""题目描述
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""

"""解题思路
使用动态规划的中心拓展法
注意回文串的中心可能是一个字符或者两个字符。因此，我们遍历每一个字符和每一对相邻的字符
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            # 注意r不能等于n
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
            return r - l - 1

        # 特判
        if (not s or len(s) == 1):
            return s
        n = len(s)
        start = 0
        end = 0
        for i in range(n):
            len_1 = expand(i, i)
            len_2 = expand(i, i + 1)
            max_len = max(len_1, len_2)
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:(end + 1)]
