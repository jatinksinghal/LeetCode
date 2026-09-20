class Solution:
    def calPoints(self, operations: list[str]) -> int:
        r=[]
        for i in operations:
            if i=="D":
                r.append(r[-1]*2)
            elif i=="C":
                r.pop()
            elif i=="+":
                r.append(r[-1]+r[-2])
            else:
                r.append(int(i))
        return sum(r)