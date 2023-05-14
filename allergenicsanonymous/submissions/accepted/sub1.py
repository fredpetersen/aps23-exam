from collections import defaultdict 
from flow import flow

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
  allergens = set(input().split())
  customer = "c" + "".join(allergens)
  # print("NY CUSTOMER", customer)
  for gin,allergenics in gins.items():
    # print(gin, allergenics)
    if len(allergens&allergenics)==0:
      graph[gin][customer] += 1
  for tonic,allergenics in tonics.items():
    if len(allergens&allergenics)==0:
      graph[customer][tonic] += 1

# print(graph)

fv,fg,cut = flow(graph, "start", "end")
print(fv)
# print(fg)