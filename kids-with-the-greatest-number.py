#Author : Umar Qureshi
#Leetcode's Kids With the Greatest Number Python Solution
#Problem Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_elem = max(candies)
        listi = []
        for x in candies:
            if x + extraCandies >= max_elem:
                listi.append(True)
            else:
                listi.append(False)
        return listi