class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        a = str(x)
        b = a[::-1]
        c = int(b)        
        if(x == c):
            return True
        else:
            return False