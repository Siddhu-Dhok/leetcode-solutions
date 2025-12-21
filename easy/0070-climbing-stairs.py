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

"""
Leet code Solution:

# Intuition
Well the time complexity is O(n^2), yeah unefficient.
But i used my Mathematics skills into it.
Never been proud of my code!
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
So maximum steps would be by considering only 1 step which would  be n and minimum would be (n // 2) or (n // 2 + 1), even and odd repectively.

So from maximum to minimum steps the number of 2's will go from [0, n//2].
Mathematically we'll consider the approach of permutations.
ex, 
for n = 6, let no. of 2's == 1
therefore number of possible combos for 1: 2's and 4: 1's (1*2 + 4*1 == 6) is
5! / (1! * 4!)
Here 5! represents total arrangements of 5 digits, but there are four 1's -repetative so diving by repatative numbers

By iterating through Maximum step to Minimum step number of 2's will go [0, n // 2] incrementing by 1 and number of 1's will go from [n, 0] depending on step and number of 2's

Final answer will be summation of all the steps.

ex, n = 6, therefore
ans = [6! / (6! * 0!)] + [5! / (4! * 1!)] + [4! / (2! * 2!)] + [3! / (0! * 3!)]

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n^2)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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


```# Intuition
Well the time complexity is O(n^2), yeah unefficient.
But i used my Mathematics skills into it.
Never been proud of my code!
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
So maximum steps would be by considering only 1 step which would  be n and minimum would be (n // 2) or (n // 2 + 1), even and odd repectively.

So from maximum to minimum steps the number of 2's will go from [0, n//2].
Mathematically we'll consider the approach of permutations.
ex, 
for n = 6, let no. of 2's == 1
therefore number of possible combos for 1: 2's and 4: 1's (1*2 + 4*1 == 6) is
5! / (1! * 4!)
Here 5! represents total arrangements of 5 digits, but there are four 1's -repetative so diving by repatative numbers

By iterating through Maximum step to Minimum step number of 2's will go [0, n // 2] incrementing by 1 and number of 1's will go from [n, 0] depending on step and number of 2's

Final answer will be summation of all the steps.

ex, n = 6, therefore
ans = [6! / (6! * 0!)] + [5! / (4! * 1!)] + [4! / (2! * 2!)] + [3! / (0! * 3!)]

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n^2)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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


```
"""
