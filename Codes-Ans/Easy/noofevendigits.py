nums=[12,345,2,6,7896]
ans=0
for i in nums:
    count=0
    while i!=0:
        i=i/10
        count+=1
    if(count%2==0):
        ans+=1
print(ans)