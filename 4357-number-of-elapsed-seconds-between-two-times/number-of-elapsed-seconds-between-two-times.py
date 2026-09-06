class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        a=startTime.split(":")
        b=endTime.split(":")
        t1,t2=0,0
        for i in range(len(a)):
            t1+=int(a[i])*(60**(len(a)-1-i))
            t2+=int(b[i])*(60**(len(a)-1-i))
        return(max(t1,t2)-min(t1,t2))