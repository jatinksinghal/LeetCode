class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        a=purchaseAmount%10
        b=purchaseAmount//10
        if a>=5:
            b+=1
        return 100- b*10