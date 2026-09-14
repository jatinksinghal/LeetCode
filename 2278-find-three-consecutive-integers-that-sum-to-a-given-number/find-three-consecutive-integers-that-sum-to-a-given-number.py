class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a=(num-3)
        if a%3==0:
            print([a//3,a//3 +1, a//3 +2])
            return [a//3,a//3 +1, a//3 +2]
        else:
            return[]
        # i=1
        # while i>0:
        #     if i+i+i+1+2==num:
        #         return list[i,i+1,i+2]
        #         break
        #     elif i+2+i+i+1>num:
        #         break
        #         return []
        #     i+=1