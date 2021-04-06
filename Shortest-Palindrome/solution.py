class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        reverse = s[::-1]
        total = reverse + s
        length = len(s)
        for i in range(length-1):
            output = reverse[0:(i+1)] + s
            if output == output[::-1]:
                return output
