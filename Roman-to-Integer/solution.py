class Solution:
    def romanHelper (self, letter: str):
        if letter == "I":
            return 1
        if letter == "V":
            return 5
        if letter == "X":
            return 10
        if letter == "L":
            return 50
        if letter == "C":
            return 100
        if letter == "D":
            return 500
        if letter == "M":
            return 1000
        
    def romanToInt(self, s: str) -> int:
        letters = [letter for letter in s]
        output = 0
        for i in range(len(letters)):
            curr_num = self.romanHelper(letters[i])
            next_num = self.romanHelper(letters[min(i+1, (len(letters)-1))])
            if curr_num < next_num:
                curr_num *= -1
            output += curr_num
        return output
