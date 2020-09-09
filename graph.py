from collections import defaultdict
graph=defaultdict(list)
def findpath(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath=findpath(graph, node, end, path)
            if newpath:
                return newpath
            return 0
def addedge(graph,u,v):
    graph[u].append(v)
if __name__=='__main__':
    n=int(input())
	Nodes=[]
	for i in range(0,n):
    	Nodes.append(input())
	e=int(input())
	for i in range(0,e):
    	a=list(map(int,input().split()))
    	addedge(graph,a[0],a[1])
	follower=int(input())
	following=int(input())
	if findpath(graph,follower,following):
    	print(1)
	else:
    	print(0)
	
   
