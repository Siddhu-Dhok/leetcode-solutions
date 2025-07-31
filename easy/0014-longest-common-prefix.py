# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix

