#Author : Umar Qureshi
#Leetcode's Longest Palindromic Substring Python3 Solution
# Problem Link : https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = ['#']
        for char in s:
            string += [char, '#']
        LPS = [0 for _ in range(len(string))]
        C = 0
        R = 0

        for i in range(len(string)):
            iMirror = 2*C - i
            if R > i:
                LPS[i] = min(R-i, LPS[iMirror])
            else:
                LPS[i] = 0
            try:
                while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                    LPS[i] += 1
            except:
                pass

            if i + LPS[i] > R:
                C = i
                R = i + LPS[i]

        r, c = max(LPS), LPS.index(max(LPS))
        ss= ""
        for x in string[c - r : c + r]:
            if x == "#":
                pass
            else:
                ss += x
        return ss
        