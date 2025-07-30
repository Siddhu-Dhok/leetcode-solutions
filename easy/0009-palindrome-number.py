#My_sol
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        z= x
        while (x > 0):
            y = y*10 + x%10
            x = x//10

        if (y == z):
            return True
        else:
            return False

#Improved with Chatgpt
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
        
#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10
        
#         return x == reversed_half or x == reversed_half // 10
        

