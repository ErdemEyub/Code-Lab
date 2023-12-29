class Solution:
    def isPalindrome(self,number):
        if number < 0:
            return False
        stringed_number = str(number)
        stringed_list = list(stringed_number)
        reversed_sl = stringed_list[::-1]
        if stringed_list == reversed_sl:
            return True
        else:
            return False
        # Testing the function

print(Solution.isPalindrome(Solution,121))
print(Solution.isPalindrome(Solution,-121))
print(Solution.isPalindrome(Solution,10))
print(Solution.isPalindrome(Solution,1221))

