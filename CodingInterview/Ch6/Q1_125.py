class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = []
        for i in s:
            if i.isalpha() or i.isdigit():
                temp.append(i)

        return temp == temp[::-1]