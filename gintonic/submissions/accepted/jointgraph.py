#! usr/bin/env python3
from collections import defaultdict 

def bfs(graph,src,dest,mincap=0): # returns path to dest
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > mincap and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))
    
def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity
    while True:
        ispath,p_or_seen = bfs(graph,src,dest,mincap)
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
        p = p_or_seen
        saturation = min( graph[u][v] for u,v in p )
        
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

g,t,n = map(int,input().split())
gins = defaultdict(set)
graph = defaultdict(lambda: defaultdict(int))

for i in range(g):
  amount, *allergens_list = input().split()
  allergens = set(allergens_list)
  gin = "g" + "".join(allergens)
  graph["start"][gin] += int(amount)
  gins[gin] = allergens

tonics = defaultdict(set)
# print("gins", gins)

for i in range(t):
  amount, *allergens_list = input().split()
  allergens = set(allergens_list)
  tonic = "t" + "".join(allergens)
  graph[tonic]["end"] += int(amount)
  tonics[tonic] = allergens
  
customers = defaultdict(set)
# print("tonics", tonics)

for i in range(n):
  _, *allergies = input().split()
  allergies = set(allergies)
  customer = "c" + "".join(allergies)
  customerStart = customer+"s"
  customerEnd = customer+"e"
  graph[customerStart][customerEnd] += 1
  # print("NY CUSTOMER", customer)
  for gin,allergens in gins.items():
    # print(gin, allergens)
    if len(allergies&allergens)==0:
      graph[gin][customerStart] += 1
  for tonic,allergens in tonics.items():
    if len(allergies&allergens)==0:
      graph[customerEnd][tonic] += 1

# print(graph)

fv,fg,cut = flow(graph, "start", "end")
print(fv)
# print(fg)


