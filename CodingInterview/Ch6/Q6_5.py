#TLE
class Solution:

    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if len(s[i:j + 1]) >= longest:
                        ans = s[i:j + 1]
                        longest = len(s[i:j + 1])
        return ans


