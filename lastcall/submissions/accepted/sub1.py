# Some accepted python solution (This would currently only socres 1 and 2)
from collections import defaultdict 
from flow import flow

n = int(input())
ingredients = defaultdict(int)

for _ in range(n):
  ing, num = input().split()
  ingredients[ing] = int(num)

m = int(input())
drinks = defaultdict(list)
for _ in range(m):
  drink, *ings = input().split()
  drinks[drink] = ings

j = int(input())
customers = defaultdict(list)
for _ in range(m):
  customer, *drink_prefs = input().split()
  customers[customer] = drink_prefs


graph = defaultdict(lambda : defaultdict(int))

for (ing, num) in ingredients.items():
  graph["start"][ing] = num

for drink, ings in drinks.items():
  for ing in ings:
    graph[ing][drink] = 100

for cust, prefs in customers.items():
  for pref in prefs:
    graph[pref][cust] = 1
  graph[cust]["end"] = 1

fv,fg,cut = flow(graph, "start", "end")
print(fv)
print(fg)
