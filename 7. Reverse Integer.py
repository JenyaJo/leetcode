class Solution:

    def reverse(self, x: int) -> int:
        s = str(x)

        def rev(st: str):
            return st[::-1]

        if s[0] == '-':
            sol = int('-' + rev(s[1:]))
            if sol < -(2 ** 31 - 1):
                return 0
            return sol
        else:
            if int(rev(s)) > 2 ** 31 - 1:
                return 0
            return int(rev(s))
