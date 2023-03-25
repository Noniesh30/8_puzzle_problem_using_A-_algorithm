#8 puzzle problem using a* algorithm
import pandas as pd
import numpy as np
import math 

#find

def find(dfi):
  col=dfi.columns 
  for i in col:
    x=dfi[i].values 
    for j in range(len(x)):
      if(x[j]==0):
        x1=i 
        y1=j
        # print('({},{})'.format(x1,y1))
        break
  return x1,y1

#heuristic calculation based on misplaced pieces

def heuristic(dfi,dff):
  col=dfi.columns 
  sum=0
  for i in col:
    x=dfi[i].values 
    y=dff[i].values
    for j in range(len(x)):
      if(x[j]!=y[j]):
        sum+=1 
  return sum

# locating neighbor 

def distance(pos,pos1):
  x=abs(pos[0]-pos1[0])**2 
  y=abs(pos[1]-pos1[1])**2 
  d=x**2+y**2 
  d=math.sqrt(d)
  return d

def neighbor(pos):
  pis=[]
  n=3 
  lis=[]
  for i in range(n):
    for j in range(n):
        ris=[]
        ris.append(i)
        ris.append(j)
        lis.append(ris)
  allcor=lis
  for i in allcor:
    dis=distance(pos,i)
    if(dis==1):
      pis.append(i)
#   print(pis)
  return pis

#creating statespace
def swap(x,y):
  a=x 
  x=y 
  y=a 
  return x,y

def best(lis,dfi,positions,x1,y1):
  x=np.argmin(lis)
  x3=positions[x][0]
  y3=positions[x][1]
  dfi[x1][y1],dfi[x3][y3]=swap(dfi[x1][y1],dfi[x3][y3])
  print(dfi)
  print("\n")

def statespace(positions,dfi,x1,y1):
  lis=[]
  for i in positions: 
    x2=i[0]
    y2=i[1] 
    dfi[x1][y1],dfi[x2][y2]=swap(dfi[x1][y1],dfi[x2][y2])
    h=heuristic(dfi,dff)
    lis.append(h)
    dfi[x1][y1],dfi[x2][y2]=swap(dfi[x1][y1],dfi[x2][y2])
  best(lis,dfi,positions,x1,y1)

#creating solution

def solve(dfi,dff,sum,pos1):
 
  h=heuristic(dfi,dff)
  pos=[]
  if(h==0):
    print("Hence completed")
  elif(h!=0):
    print("Level {}".format(sum))
    x1,y1=find(dfi)
    pos.append(x1)
    pos.append(y1)
    # print(x1,y1)
    positions=neighbor(pos)
    if(sum==0):
      pos1.append(x1)
      pos1.append(y1)
    elif(sum!=0):
      positions.remove(pos1)
      pos1.clear()
      pos1.append(x1)
      pos1.append(y1)
    statespace(positions,dfi,x1,y1)
    sum+=1
    solve(dfi,dff,sum,pos1)
#main
initial_state=[[2,8,3],[1,6,4],[7,0,5]]
final_state=[[1,2,3],[8,0,4],[7,6,5]]
dfi=pd.DataFrame(initial_state)
print("Initial_state")
print(dfi)
dff=pd.DataFrame(final_state)
print("\n")
print("Final_state")
print(dff)
print("\n")
sum=0
pos1=[]
solve(dfi,dff,sum,pos1)

