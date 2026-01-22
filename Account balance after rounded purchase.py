
def bal(purchaseAmount):
    balance = 100
    while purchaseAmount%10 != 0 or purchaseAmount == 0:
        purchaseAmount+=1
    balance-=purchaseAmount
    return balance
print(bal(4))