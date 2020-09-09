from collections import defaultdict
graph=defaultdict(list)
def addedge(graph,u,v):
    for i in v:
        graph[u].append(i)
def short(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    shortest=None
    for node in graph [start]:
        if node not in path:
            newpath=short(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest=newpath
    return shortest
if __name__=='__main__':
    n=int(input())
    nodes=[]
    for i in range(0,n):
        nodes.append(input())
    e=int(input())
    for i in range(0,e):
        a=list(map(int, input().split()))
        a0=a[0]
        a.pop(0)
        addedge(graph,a0,a)
    follower=int(input())
    following=int(input())
    l=short(graph,follower,following)
    if l:
        print(len(l))
    
