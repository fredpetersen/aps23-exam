#! usr/bin/env python3
from collections import defaultdict 
from time import time # Benchmark

def bfs(graph,src,dest): # returns path to dest
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > 0 and v not in parent:
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

def dfs(graph,src,dest):
    parent = {src:src}
    nodes_to_check = [src]
    while nodes_to_check:
        node = nodes_to_check.pop()
        for v, cap in graph[node].items():
            if cap > 0 and v not in parent:
                parent[v] = node
                nodes_to_check.append(v)
                if v == dest:
                    p = []
                    current_vertex = dest
                    while src != current_vertex:
                        p.append((parent[current_vertex],current_vertex))
                        current_vertex = parent[current_vertex]
                    return (True,p)
    return (False, set(parent))
    
def flow(orggraph, src,dest):
    graph = orggraph.copy()
    current_flow = 0
    while True:
        ispath, p = dfs(graph,src,dest)
        if not ispath:
            return current_flow
        saturation = min( graph[u][v] for u,v in p )
        
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation
            
def has_shared_element(set1, set2):
    if len(set1) < len(set2):
        for elem in set1:
            if elem in set2:
                return True
    else:
        for elem in set2:
            if elem in set1:
                return True
    return False
    

g,t,n = map(int,input().split())
gins = defaultdict(set)
graph = defaultdict(lambda: defaultdict(int))


start_time = time()
for i in range(g):
  amount, *allergens_list = input().split()
  allergens = set(allergens_list)
  gin = "g" + "".join(allergens)
  graph["start"][gin] += int(amount)
  gins[gin] = allergens

tonics = defaultdict(set)
# print("gins", gins)
# print("Loading gins took", time()-start_time)
inter_time = time()

for i in range(t):
  amount, *allergens_list = input().split()
  allergens = set(allergens_list)
  tonic = "t" + "".join(allergens)
  graph[tonic]["end"] += int(amount)
  tonics[tonic] = allergens
  
customers = defaultdict(set)
# print("tonics", tonics)

# print("Loading tonics took", time()-inter_time)
inter_time = time()

cum_hashing_time = 0
cum_graph_time = 0

for i in range(n):
  hash_start_time = time()
  name, *allergies = input().split()
  allergies = set(allergies)
  customer = name
  customerStart = customer+"s"
  customerEnd = customer+"e"
  cum_hashing_time += time()-hash_start_time
  
  graph_start_time = time()
  graph[customerStart][customerEnd] += 1
  if graph[customerStart][customerEnd] > 1:
      continue
  # print("NY CUSTOMER", customer)
  for gin,allergens in gins.items():
    # print(gin, allergens)
    if not has_shared_element(allergies, allergens):
      graph[gin][customerStart] = 1
  for tonic,allergens in tonics.items():
    if not has_shared_element(allergies, allergens):
      graph[customerEnd][tonic] = 1
  cum_graph_time += time()-graph_start_time
      
# print("Loading customers and constructing graph took", time()-inter_time)
# print("Hashing took", cum_hashing_time)
# print("Graphing took", cum_graph_time)
inter_time = time()

# print(graph)

fv= flow(graph, "start", "end")
# print("Running flow took", time()-inter_time)
# print("TOTAL COMPLETION TIME", time() - start_time)
print(fv)
# print(fg)


