n = [7,4,3,9,1,8,5,2,6]
k=3
avg=0
output=[]
sub=0
count = 2*k+1
for i in range(k):
    output.append(-1)
for i in range(k,len(n)-k):
    for j in range(i-k,i+k+1):
        sub+=n[j]
    output.append(sub//count)
    sub=0
for i in range(len(n)-k,len(n)):
    output.append(-1)
print(f"result is: {output}")