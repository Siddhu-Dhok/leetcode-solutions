# Problem: 70. Climbing Stairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/climbing-stairs/

import math # for factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # assigning seperate stoping point according to even/odd
        if n % 2 == 0:
            stop_val = n // 2 - 1
        else:
            stop_val = n // 2

# iterate from n to n // 2
# no. of 2's: [0, n // 2], 1's: [n, 0]

        for i in range(n, stop_val, -1):
            j = i
            ans += math.factorial(i)/(math.factorial(n - i) * math.factorial(2*i - n))
        
        return int(ans)
import math # for factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # assigning seperate stoping point according to even/odd
        if n % 2 == 0:
            stop_val = n // 2 - 1
        else:
            stop_val = n // 2

# iterate from n to n // 2
# no. of 2's: [0, n // 2], 1's: [n, 0]

        for i in range(n, stop_val, -1):
            j = i
            ans += math.factorial(i)/(math.factorial(n - i) * math.factorial(2*i - n))
        
        return int(ans)


"""
The problem was factorials.

Instead of computing factorials repeatedly, we compute combinations iteratively using:

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        c = 1  # C(n, 0)

        for k in range(0, n // 2 + 1):
            if k > 0:
                c = c * (n - (k - 1)) // k
            ans += c

        return ans

✔ No factorial
✔ No floats
✔ O(n) time, O(1) space

# optimal using fibonacci:

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b

"""
