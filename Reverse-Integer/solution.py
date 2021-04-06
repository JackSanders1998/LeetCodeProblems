class Solution:
    def reverse(self, x: int) -> int:
        
        # can't store 64 bit integers
        if (x < (-2 ** 31)) or (x > (2 ** 31)):
            return 0
        
        # account for inputs < 0 (if input<0 -> sign=-1)
        # absolute value of x
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
            
        # list of digits in reversed order
        output_list = []
        while x != 0:
            right_digit = x % 10
            x = (x - right_digit) // 10
            output_list.append(right_digit)
        
        # int value of reversed list
        output_num = 0
        index = len(output_list) - 1
        for num in output_list:
            output_num += num * (10 ** index)
            index -= 1
        
        # account for 32-bit int range
        if output_num > (2 ** 31):
            return 0
        else:
            return output_num * sign    # account for sign (either 1 or -1)
