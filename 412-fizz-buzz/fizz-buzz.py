class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        i=0
        while i<n:
            i+=1
            if i%3==0 and i%5==0:
                a.append("FizzBuzz")
                pass
            elif i%3==0:
                a.append("Fizz")
                pass
            elif i%5==0:
                a.append("Buzz")
                pass
            else:
                a.append(str(i))
        return a
