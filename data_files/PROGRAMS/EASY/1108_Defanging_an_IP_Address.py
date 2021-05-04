# ID : 1108
# Title : Defanging an IP Address
# Difficulty : EASY
# Acceptance_rate : 88.4%
# Runtime : 32 ms
# Memory : 13.9 MB
# Tags : String
# Language : python3
# Problem_link : https://leetcode.com/problems/defanging-an-ip-address
# Premium : 0
# Notes : -
###

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
