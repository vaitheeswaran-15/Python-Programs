n = 10
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
total={}
arr=set()
for i in range(n):
    pair_count=1
    if ar[i] in arr:
        continue
    for j in range(i+1,n):
        arr.add(ar[i])
        if ar[i]==ar[j]:
            pair_count+=1
            total[ar[i]]=pair_count
print(total)
count=0
total_count=[]
for j in arr:
    if j not in total:
        continue
    else:
        total_count.append(total[j]//2)
print(total_count)
return_count=0
for i in total_count:
    return_count+=i
print(return_count)        
