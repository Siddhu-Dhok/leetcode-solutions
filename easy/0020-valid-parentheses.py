# Problem: 20. Valid Parentheses
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)
        sid = {('(', ')'), ('[', ']'), ('{', '}')}

        while True:
            changed = False
            i = 0
            while i < len(l) - 1:
                if (l[i], l[i + 1]) in sid:
                    del l[i:i+2]   # remove valid pair
                    changed = True
                    break          # restart from beginning
                else:
                    i += 1
            if not changed:
                break

        return not l


#GPT solution using stack

#class Solution:
#    def isValid(self, s: str) -> bool:
#        stack = []
#        matching = {')': '(', ']': '[', '}': '{'}
#
#        for char in s:
#            if char in matching.values():  # Opening bracket
#                stack.append(char)
#            elif char in matching:  # Closing bracket
#                if not stack or stack[-1] != matching[char]:
#                    return False
#                stack.pop()
#            else:
#                return False  # Invalid character (optional check)
#
#        return not stack  # True if all brackets matched and closed
