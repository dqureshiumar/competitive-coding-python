#Author : Umar Qureshi
#Leetcode's Find Numbers with Even Number of Digits Python3 Solution
# Problem Link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for x in nums:
            s = str(x)
            if len(s) % 2 == 0:
                c += 1
        return c