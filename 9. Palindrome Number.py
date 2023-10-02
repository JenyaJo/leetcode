class Solution:

    def is_palindrome(self, x: int) -> bool:
        word = str(x)
        if len(word) == 1:
            return True
        for i in range(0, len(word) // 2):

            if word[i] != word[-1 * (i + 1)]:
                return False
        return True
