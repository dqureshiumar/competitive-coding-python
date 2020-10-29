#Author : Umar Qureshi
#Leetcode's Decompress Run-Length Encoded List Python3 Solution
# Problem Link : https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        listi = []
        lent = len(nums)
        i = 0
        while lent:
            for j in range(nums[i]):
                listi.append(nums[i+1])
            i += 2
            lent -= 2
        return listi