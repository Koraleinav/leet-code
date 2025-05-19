"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # first way, using slicing

        return (str(x)[::-1]) == str(x)


    # second way, using an array


        if  x < 0:
            return False


        nums_arr= []
        while x != 0:
            nums_arr.append(x % 10)
            x = x // 10

        if len(nums_arr) == 1:
            return True

        if len(nums_arr) % 2 != 0:
            nums_arr.remove(nums_arr[len(nums_arr) // 2])


        new_arr_len = len(nums_arr)
        left_arr = []


        for index in range(len(nums_arr) // 2):
            left_arr.append(nums_arr[index])
        
        for i in range(len(left_arr)):
            print(left_arr[i])

                

        for i in range(new_arr_len // 2):
            nums_arr.remove(nums_arr[i])
        right_arr = nums_arr.copy()

        for i in range(len(right_arr)):
            print(right_arr[i])

        for i in range(new_arr_len // 2):
            if left_arr[i] != right_arr[len(right_arr) - i - 1]:
                return False

        return True

        
    # third way, reversing the number

        if(x < 0):
            return False

        reverse_num = 0
        temp = x 
        while(temp != 0):
            reverse_num = reverse_num * 10 + (temp % 10)
            temp = temp // 10

        return x == reverse_num

             
            

        






    