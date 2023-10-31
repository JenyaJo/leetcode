"""https://leetcode.com/problems/greatest-common-divisor-of-strings"""

def gcdOfStrings(str1: str, str2: str) -> str:
    short_w = min(str1, str2)
    short_for_check = min(str1, str2)
    long_w = max(str1, str2)
    while short_w != '':
        if len(long_w) % len(short_w) == 0:
            base = int(len(long_w) / len(short_w))
            if short_w * base == long_w and short_w * int(len(short_for_check) / len(short_w)) == short_for_check:
                return short_w
        short_w = short_w[:-1]
    return ''