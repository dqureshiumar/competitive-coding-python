#Author : Umar Qureshi
#Leetcode's Kids With the Greatest Number Python Solution

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