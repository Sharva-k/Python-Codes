nums = [3,1,-2,-5,2,-4]

pos , neg = 0,1
res = [0] * len(nums)
for i in nums:
    if i > 0:
        res[pos] = i
        pos+=2
    elif i<0:
        res[neg] = i
        neg+=2
print(f"resulting array of sorted pos and neg integers is: {res}")
