#Author : Umar Qureshi
#Leetcode's Shuffle the Array Python3 Solution
# Problem Link : https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        listi = []
        i = 0
        j = n
        while n:
            listi.append(nums[i])
            listi.append(nums[j])
            i += 1
            j += 1
            n -= 1
        return listi