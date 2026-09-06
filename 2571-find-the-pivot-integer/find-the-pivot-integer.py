class Solution:
    def pivotInteger(self, n: int) -> int:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        for i in range(1,n+1):
            a=sum(nums[:i])
            b=sum(nums[i-1:])
            if a==b:
                return i
                break
        else:
            return -1