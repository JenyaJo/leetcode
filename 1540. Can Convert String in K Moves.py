'''https://leetcode.com/problems/can-convert-string-in-k-moves/'''
import string

def canConvertString(self, s: str, t: str, k: int) -> bool:
    if len(s) != len(t):
        return False
    abc_dict = {letter: index + 1 for index, letter in enumerate(list(string.ascii_lowercase))}
    s_list = list(s)
    t_list = list(t)
    cache = set()
    circles = {}
    for index, letter in enumerate(s_list):
        if s_list[index] == t_list[index]:
            continue
        div = abc_dict[t_list[index]] - abc_dict[s_list[index]]
        if div < 0:
            div += 26
        if div > k:
            return False
        if div not in cache:
            cache.add(div)
            circles[div] = 1
        else:
            next_div = div + 26 * circles[div]
            if next_div > k:
                return False
            cache.add(div + 26 * circles[div])
            circles[div] += 1
    return True
