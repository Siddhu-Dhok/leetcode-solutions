class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0

        ref = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for i in s:
            val += ref[i]

        return val


#Gpt:
#class Solution:
#    def romanToInt(self, s: str) -> int:
#        roman = {
#            "I": 1, "V": 5, "X": 10,
#            "L": 50, "C": 100, "D": 500, "M": 1000
#        }
#        
#        total = 0
#        prev_value = 0
#        
#        for char in reversed(s):
#            current = roman[char]
#            if current < prev_value:
#                total -= current
#            else:
#                total += current
#            prev_value = current
#        
#        return total
#
#🧠 How It Works:
#    •    Loop is reversed so subtraction happens correctly (e.g., for "IV" you see "V" first, then subtract "I").
#    •    If a numeral is less than the previous (right) numeral → subtract it.
#    •    Else → add it.
