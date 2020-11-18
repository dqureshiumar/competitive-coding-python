#Author : Umar Qureshi
#Maximum Product of Three Numbers Python3 Solution
# Problem Link : https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2 = -2147483648, -2147483648
        min1, min2, min3 = 2147483648, 2147483648, 2147483648
        for x in nums:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x
        return max(max1 * min1 * min2, max1 * max2 * max3)