import os
import snap
Rnd=snap.TRnd(42)
Rnd.Randomize()
cwd=os.getcwd()
V=snap.TIntV()
G=snap.LoadEdgeList(snap.PUNGraph, "com-amazon.ungraph.txt", 0, 1)
for NI in G.Nodes():
	Id=NI.GetId()
	if (Id%4==0):
		V.Add(Id)

G1=snap.GetSubGraph(G, V)
os.chdir(cwd+"/subgraphs")
snap.SaveEdgeList(G1, "amazon.elist")
os.chdir(cwd)