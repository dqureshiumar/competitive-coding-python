#Author : Umar Qureshi
#Leetcode's XOR Operation in an Array Python3 Solution
# Problem Link : https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        x = 0
        for y in nums:
            x = x ^ y
        return x