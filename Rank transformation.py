arr=[37,12,28,9,100,56,80,5,12]
output=[]
rank = 1
for i in range(len(arr)):
    curr = arr[i]
    for j in range(len(arr)):
        if curr > arr[j]:
            rank+=1
    output.append(rank)
    rank = 1
print(output)
