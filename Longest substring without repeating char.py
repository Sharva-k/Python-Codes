s="abcabcbb"
seen = {}
left = 0
count =0 
for i in range(len(s)):
    while s[i] in seen:
        seen.remove(s[left])
        left+=1

    seen.add(s[i])
    count = max(count,i - left+1)
