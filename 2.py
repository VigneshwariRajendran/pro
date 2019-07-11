kk,jj=input().strip().split()
jj=int(jj)
k=0
while k<len(kk)-1 and jj:
  if(kk[k]>kk[k+1]):
    jj-=1
    kk=kk[:k]+kk[k+1:]
    if(k!=0):
      k-=1
  else:
    k+=1
lk=kk[:len(kk)-jj]
print(lk)
    
