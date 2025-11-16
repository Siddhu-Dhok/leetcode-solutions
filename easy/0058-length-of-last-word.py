# Problem: 58. Length of Last Word
# Difficulty: Easy
# URL: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        flag = 1

        for i in range(len(s)):
            if s[i] == ' ':
                flag = 0
            else:
                if flag == 0:
                    count = 0
                count += 1
                flag = 1

        return count

#class Solution:
#    def lengthOfLastWord(self, s: str) -> int:
#        count = 0
#        i = len(s) - 1
#
#        # Skip trailing spaces
#        while i >= 0 and s[i] == ' ':
#            i -= 1
#
#        # Count characters of last word
#        while i >= 0 and s[i] != ' ':
#            count += 1
#            i -= 1
#
#        return count


# One liner:
# return len(s.rstrip().split()[-1])
