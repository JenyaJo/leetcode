class Solution:
    def isPalindrome(self, s: str) -> bool:
        digits = '0123456789'
        string = ''.join(i.lower() for i in s if i.isalpha() or i in digits)

        for i in range(0, len(string) // 2):
            if string[i] != string[-1 * (i + 1)]:
                return False
        return True
