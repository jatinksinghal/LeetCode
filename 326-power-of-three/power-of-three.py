class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0 or n==-1 or n<0:
            return False
        elif 3**21/n %3==0:
            return True
        
        else:
            return False
        # if n <= 0:
        #     return False
        # if n == 1:
        #     return True
        # if n % 3 != 0:
        #     return False
        # return self.isPowerOfThree(n//3)