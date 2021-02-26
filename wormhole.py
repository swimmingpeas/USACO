"""
ID: benzhao1
LANG: PYTHON3
TASK: wormhole
"""
from math import *
import itertools

def infloop (pairings,values):
    for loc in values:
        count=0
        loc1=loc
        flag=True
        while(count<14 and flag):
            if values.__contains__((loc1[0]+1,loc1[1])):
                count+=1
                index=values.index((loc1[0]+1,loc1[1]))
                loc1=values[pairings[index]]
            else:
                flag=False
        if(flag):
            return True
    return False
inputfile=open("wormhole.in","r")
outputfile=open("wormhole.out", "w")
n=int(inputfile.readline())
q1=inputfile.readline().split()
locations0=[q1[1]]
locations1=[1]
for i in range (n-1):
    q=inputfile.readline().split()
    if locations0.__contains__(q[1]):
        locations1[locations0.index(q[1])]+=1
    else:
        locations0.append(q[1])
        locations1.append(1)
positions=[]
for i in range (len(locations1)):
    for j in range (locations1[i]):
        positions.append((j,i))
match=[]
for i in range(n):
    match.append(-1)
def solution():
    answer=0
    flag4=True
    for i in range (n):
        if(match[i]==-1):
            flag4=False
            break
    if flag4:
        if(infloop(match,positions)):
            return 1
        else:
            return 0
    for j in range(i+1,n):
        if match[j]==-1:
            match[i]=j
            match[j]=i
            answer+=solution()
            match[i]=-1
            match[j]=-1
    return answer

ans=solution()
print(ans)
outputfile.write(str(ans)+'\n')
outputfile.close()