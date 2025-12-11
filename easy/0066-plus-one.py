#Problem: 66. Plus one
# Difficulty: Easy
# URL: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = num * 10
            num = num + i
        
        num = num + 1

        lst = list()

        while (num != 0):
            lst.insert(0, num % 10)
            num = num // 10

        return lst


#cleaner
#using append is better and then reversing it
#
#class Solution:
#    def plusOne(self, digits: List[int]) -> List[int]:
#        num = 0
#        for i in digits:
#            num = num * 10 + i
#        
#        num += 1
#
#        lst = []
#        while num != 0:
#            lst.insert(0, num % 10)
#            num //= 10
#
#        return lst
#        
#Best
#
#class Solution:
#    def plusOne(self, digits: List[int]) -> List[int]:
#        i = len(digits) - 1
#
#        while i >= 0:
#            if digits[i] == 9:
#                digits[i] = 0
#            else:
#                digits[i] += 1
#                return digits
#            i -= 1
#        
#        return [1] + digits
