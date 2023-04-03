class Solution:
    def romanToInt(self, s: str) -> int:

        #largest to smallest: add them up
        #smaller before large: subtract smaller


        
        roman = { 

        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000     

        }
     
        output = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                output -= roman[s[i]]

            else: 

                output += roman[s[i]]

        return output