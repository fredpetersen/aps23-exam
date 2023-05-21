#! usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
g,t,n = map(int,input().split())
gins = []
tonics = []

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

for i in range(g):
  amount, *allergens_list = input().split()
  allergens_list = set(allergens_list)
  for _ in range(int(amount)):
    gins.append(allergens_list)
  

# print("gins", gins)

for i in range(t):
  amount, *allergens_list = input().split()
  allergens_list = set(allergens_list)
  for _ in range(int(amount)):
    tonics.append(allergens_list)
    
    
maxMatchings = 0
customers = []

for i in range(n):
  name, *allergens_list = input().split()
  allergens_list = set(allergens_list)
  customers.append(allergens_list)

def findMatchings(rem_customers, rem_gins, rem_tonics):
  maxMatches = 0
  matches = 0
  for customer_allergens in rem_customers:
    for gin in rem_gins:
      for tonic in rem_tonics:
        if not has_shared_element(customer_allergens, gin) and not has_shared_element(customer_allergens,tonic):
          matches += 1
          new_rem_customers =rem_customers.copy()
          new_rem_customers.remove(customer_allergens)
          new_rem_gins = rem_gins.copy()
          new_rem_gins.remove(gin)
          new_rem_tonics = rem_tonics.copy()
          new_rem_tonics.remove(tonic)
          matches += findMatchings(new_rem_customers, new_rem_gins, new_rem_tonics)
          maxMatches = max(maxMatches, matches)
          matches = 0
          
  return maxMatches

print(findMatchings(customers,gins,tonics))