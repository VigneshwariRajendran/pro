qw=int(input())
ad=[]
for i in range(0,qw):
  io=input()
  ad.append(io)
ff=[]
for i in zip(*ad):
  if(i.count(i[0]==len(i))):
    ff.append(i[0])
  else:
    break
 print(''.join(ff))   
