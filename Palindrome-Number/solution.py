class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            forward_list = []
            backward_list = []
            while x != 0:
                right_digit = x % 10
                x = (x-right_digit) // 10
                forward_list.append(right_digit)
                backward_list.insert(0, right_digit)
            return forward_list == backward_list
            
