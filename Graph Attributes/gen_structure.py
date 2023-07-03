# Begin Code gen_structure.py
import sys
import snap
import os
Rnd=snap.TRnd(42)
Rnd.Randomize()
max=0 
k=0
cwd=os.getcwd()
os.chdir(cwd+"/subgraphs")
G=snap.LoadEdgeList(snap.PUNGraph, sys.argv[1], 0, 1)
os.chdir(cwd)
#1. Size of the network
print("Number of Nodes: %d \n" % (G.GetNodes()))
print("Number of Edges: %d \n" % (G.GetEdges()))
#2. Degree of nodes in the network
print("Number of Nodes with Degree=7: %d \n" % (snap.CntDegNodes(G, 7)))
Nid=snap.GetMxDegNId(G)
print("Node id(s) with highest degree: ", end="")
InDegV = snap.TIntPrV()
snap.GetNodeInDegV(G, InDegV)
for item in InDegV:
    if (item.GetVal1()==Nid):
        max=item.GetVal2()
for item in InDegV:
    if (item.GetVal2()==max):
        print("%d" % (item.GetVal1()), end="")
        k=k+1
        if (k>1):
            print(", ", end="")
print("\n")
s="deg_dist_"+sys.argv[1]
os.chdir(cwd+"/plots")
snap.PlotInDegDistr(G, s, "Undirected Graph")
os.chdir(cwd)
#3. Paths in the network
a=snap.GetBfsFullDiam(G, 10, False)
b=snap.GetBfsFullDiam(G, 100, False)
c=snap.GetBfsFullDiam(G, 1000, False)
print("Approximate full diameter by sampling 10 nodes: %d \n" % (a))
print("Approximate full diameter by sampling 100 nodes: %d \n" % (b))
print("Approximate full diameter by sampling 1000 nodes: %d \n" % (c))
fdmean=(a+b+c)/3
fdvar=(((a-fdmean)**2)+((b-fdmean)**2)+((c-fdmean)**2))/3
print("Approximate Full Diameter(mean and variance): %.4f, " % (fdmean), end="")
print("%.4f \n" % (fdvar))
a1=snap.GetBfsEffDiam(G, 10, False)
b1=snap.GetBfsEffDiam(G, 100, False)
c1=snap.GetBfsEffDiam(G, 1000, False)
print("Approximate effective diameter by sampling 10 nodes: %d \n" % (a1))
print("Approximate effective diameter by sampling 100 nodes: %d \n" % (b1))
print("Approximate effective diameter by sampling 1000 nodes: %d \n" % (c1))
fdmean1=(a1+b1+c1)/3
fdvar1=(((a1-fdmean1)**2)+((b1-fdmean1)**2)+((c1-fdmean1)**2))/3
print("Approximate Effective Diameter(mean and variance): %.4f, " % (fdmean1), end="")
print("%.4f \n" % (fdvar1))
s1="shortest_path_"+sys.argv[1]
os.chdir(cwd+"/plots")
snap.PlotShortPathDistr(G, s1, "Undirected Graph")
os.chdir(cwd)
#4. Components of the network
print("Fraction of nodes in largest connected component: %.4f \n" % (snap.GetMxSccSz(G)))
EdgeV=snap.TIntPrV()
snap.GetEdgeBridges(G, EdgeV)
print("Number of edge bridges: %d \n" % (len(EdgeV)))
ArtNIdV=snap.TIntV()
snap.GetArtPoints(G, ArtNIdV)
print("Number of articulation points: %d \n" % (len(ArtNIdV)))
s2="connected_comp_"+sys.argv[1]
os.chdir(cwd+"/plots")
snap.PlotSccDistr(G, s2, "Undirected Graph")
os.chdir(cwd)
#5. Connectivity and clustering in the network
print("Average clustering coefficient: %.4f \n" % (snap.GetClustCf(G, -1)))
print("Number of triads: %d \n" % (snap.GetTriads(G, -1)))
Id=G.GetRndNId(Rnd)
print("Clustering coefficient of random node %d: " % (Id), end="")
print("%.4f \n" % (snap.GetNodeClustCf(G, Id)))
print("Number of triads random node %d participates: " % (Id), end="")
print("%d \n" % (snap.GetNodeTriads(G, Id)))
print("Number of edges that participate in at least one triad: %d \n" % (snap.GetTriadEdges(G, -1)))
s3="clustering_coeff_"+sys.argv[1]
os.chdir(cwd+"/plots")
snap.PlotClustCf(G, s3, "Undirected Graph")
os.chdir(cwd)
# End Code