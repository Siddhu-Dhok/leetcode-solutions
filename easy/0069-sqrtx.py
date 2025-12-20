# Problem: 69. Sqet(x)
# Difficulty: Easy
# URL: https://leetcode.com/problems/sqrtx/

class Solution:
 def mySqrt(self, x: int) -> int:
    if x < 2:
        return x

    root = 0
    for i in range(1, x // 2 + 1):
        if i * i > x:
            break
        root = i

    return root

"""
Fault in this code is that it can go upto 10^9 iterations O(n)ie, 1 billion interations
so bianry search is req O(log n) ie ~30 iterations

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
"""
