#Start of program analyze_centrality.py
import os
import snap
G=snap.LoadEdgeList(snap.PNGraph, "facebook_combined.txt", 0, 1)
n=G.GetNodes()
#Calculation of centralities
a=[None]*n
b=[None]*n
i=0
for NI in G.Nodes():
    CloseCentr = snap.GetClosenessCentr(G, NI.GetId())
    b[i]=CloseCentr
    i=i+1
ans=dict(enumerate(b))
ans1=(sorted(ans.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
i=0
for k in ans1:
    a[i]=k[0]
    i=i+1
a1=[None]*n
b1=[None]*n
i=0
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(G, Nodes, Edges, 0.8)
for node in Nodes:
    a1[i]=node
    b1[i]=Nodes[node]
    i=i+1
i=0
j=0
for i in range((n-1)):
    for j in range((n-i-1)):
        if b1[j]<b1[j+1]:
            b1[j],b1[j+1]=b1[j+1],b1[j]
            a1[j],a1[j+1]=a1[j+1],a1[j]
a2=[None]*n
b2=[None]*n
i=0
PRankH = snap.TIntFltH()
snap.GetPageRank(G, PRankH)
for item in PRankH:
    a2[i]=item
    b2[i]=PRankH[item]
    i=i+1
i=0
j=0
for i in range((n-1)):
    for j in range((n-i-1)):
        if b2[j]<b2[j+1]:
            b2[j],b2[j+1]=b2[j+1],b2[j]
            a2[j],a2[j+1]=a2[j+1],a2[j]
#Retrieval of data
a3=[0]*n
a4=[0]*n
a5=[0]*n
cwd=os.getcwd()
os.chdir(cwd+"/centralities")
i=0
with open("closeness.txt", "r") as file:
    for line in file:
        for word in line.split():
            a3[i]=int(word)
            i=i+1
            break
file.close()
i=0
with open("betweenness.txt", "r") as file1:
    for line in file1:
        for word in line.split():
            a4[i]=int(word)
            i=i+1
            break
file1.close()
i=0
with open("pagerank.txt", "r") as file2:
    for line in file2:
        for word in line.split():
            a5[i]=int(word)
            i=i+1
            break
file2.close()
os.chdir(cwd)
#comparison of data
i=0
j=0
c=0
be=0
p=0
for i in range(100):
    for j in range(100):
        if a[i]==a3[j]:
            c=c+1
            break
        if a1[i]==a4[j]:
            be=be+1
            break
        if a2[i]==a5[j]:
            p=p+1
            break
print("Overlaps for Closeness Centrality: %d " % c)
print("Overlaps for Betweenness Centrality: %d " % be)
print("Overlaps for Pagerank: %d " % p)
#End of code