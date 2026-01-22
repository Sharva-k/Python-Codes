def bal(purchaseAmount):
    balance = 100
    if purchaseAmount%10 != 0 or purchaseAmount != 0:
        temp = purchaseAmount%10
        if temp>5:
            purchaseAmount-= temp
        else:
            purchaseAmount+=(10-temp)
    balance-=purchaseAmount
    return balance
pAmount = int(input("Enter purachase amount: "))
