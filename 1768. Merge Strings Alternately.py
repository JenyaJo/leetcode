"""https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75"""
def mergeAlternately(word1: str, word2: str) -> str:
    result = ''
    for i in range(min(len(word1), len(word2))):
        result += word1[i]
        result += word2[i]
    if len(word1) <= len(word2):
        result += word2[len(word1):]
    else:
        result += word1[len(word2):]
    return result