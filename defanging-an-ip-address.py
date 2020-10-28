#Author : Umar Qureshi
#Leetcode's Defanging an IP Address Python3 Solution
# Problem Link : https://leetcode.com/problems/defanging-an-ip-address/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')