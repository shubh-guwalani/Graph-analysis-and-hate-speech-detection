#Start of code gen_centrality.py
import os
from collections import deque
import snap
import math
Rnd=snap.TRnd(42)
Rnd.Randomize()
i=0
shp=0
cwd=os.getcwd()
os.chdir(cwd+"/centralities")
f=open("closeness.txt", "a+")
f1=open("betweenness.txt", "a+")
f2=open("pagerank.txt", "a+")
os.chdir(cwd)
G=snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
n=G.GetNodes()
#Closeness Centrality
a=[None]*n
a1=[None]*n
a2=[None]*n
b=[None]*n
NDH=snap.TIntH()
for NI in G.Nodes():
	a[i]=NI.GetId()
	shp=0
	shortestPath=snap.GetShortPath(G, a[i], NDH)
	for item in NDH:
		shp=shp+NDH[item]
	b[i]=((n-1)/shp)
	i=i+1
i=0
for i in range(n):
    b[i]=round(b[i],6)
ans02=dict(enumerate(b))
ans03=sorted(ans02.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
for k in ans03:
    f.write(str(k[0])+" "+str(k[1])+"\n")
f.close()	
#Betweenness Centrality
i=0
k1=0
bc=[0]*n
V=[None]*n
for NI in G.Nodes():
    V[k1]=NI.GetId()
    k1=k1+1
k2=0
#Applying Brande's Algorithm
for s in V:
    S=[]
    P=[[] for i in range(n)]
    sigma=[0]*n
    sigma[s]=1
    d=[-1]*n
    d[s]=0
    Q=deque([])
    Q.append(s)
    while len(Q)>0:
        v=Q.popleft()
        S.append(v)
        Nid=snap.TIntV()
        snap.GetNodesAtHop(G, v, 1, Nid, True)
        for w in Nid:
            if d[w]<0:
                Q.append(w)
                d[w]=d[v]+1
            if d[w]==(d[v]+1):
                sigma[w]=sigma[w]+sigma[v]
                P[w].append(v)
    delta=[0]*n
    while len(S)>0:
        w=S.pop()
        for v in P[w]:
            delta[v]=delta[v]+((sigma[v]/sigma[w])*(1+delta[w]))
        if w!=s:
            bc[w]=bc[w]+delta[w]
i=0
for i in range(n):
	bc[i]=(2*bc[i])/((n-1)*(n-2))
	bc[i]=round(bc[i],6)
ans=dict(enumerate(bc))
ans1=(sorted(ans.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
for k in ans1:
    f1.write(str(k[0])+" "+str(k[1])+"\n")
f1.close()
#Pagerank	
n1=0
for ni in G.Nodes():
    iD=ni.GetId()
    if (iD%4==0):
        n1=n1+1
alpha=0.8
err=0.00000001
converge=False
d=[0]*n
pr=[0]*n
prlast=[0]*n
i=0
j=0
for NI in G.Nodes():
    Id=NI.GetId()
    if (Id%4==0):
        d[Id]=1/n1
        pr[Id]=1/n
    else:
        d[Id]=0
        pr[Id]=1/n
while not converge:
    prlast=pr.copy()
    for Ni in G.Nodes():
        ID=Ni.GetId()
        tran=0
        Nid=snap.TIntV()
        snap.GetNodesAtHop(G, ID, 1, Nid, True)
        for v in Nid:
            t=G.GetNI(v).GetOutDeg()
            if t>0:
                tran+=pr[v]/t
            else:
                tran+=pr[v]/n
        pr[ID]=(alpha*tran)+((1.0-alpha)*d[ID])
    #Normalizing
    av=sum(pr)
    for r in pr:
        r/=av
    #Checking for convergence
    e=sum(abs(pr[j]-prlast[j]) for j in range(n))
    if e<err*n:
        converge=True
i=0
for i in range(n):
    pr[i]=round(pr[i],6)
ans2=dict(enumerate(pr))
ans3=sorted(ans2.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
for k in ans3:
    f2.write(str(k[0])+" "+str(k[1])+"\n")
f2.close()	
#End of code