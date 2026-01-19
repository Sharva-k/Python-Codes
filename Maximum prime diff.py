n=[4,2,9,5,3]

def is_prime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
ans=0

for i in range(len(n)):
    if is_prime(n[i]):
        ans+=i
        break

for i in range(len(n)-1,-1,-1):
    if is_prime(n[i]):
        ans-=i
        break
print(abs(ans))