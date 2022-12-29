def find_uniq(arr):
    # your code here
    d=dict()
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i,j in d.items():
        if j==1:
            return i
    
