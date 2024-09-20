graph={
    '5':['3','7'],
     '3':['2','4'],
     '7':['8'],
     '2':[],
     '4':['8'],
     '8':[]
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neigbour in graph[m]:
            if neigbour not in visited:
                visited.append(neigbour)
                queue.append(neigbour)
print("following is the bfs")
bfs(visited,graph,'5')