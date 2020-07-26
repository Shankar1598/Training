
def knapSack(W, items, n):

  if W==0 or n==0:
    return 0

  itemValue = items[n-1]['val']
  itemWeight = items[n-1]['wt']
  if (itemWeight > W):
    return knapSack(W, items, n-1)
  else:
    include = (itemValue + knapSack(W-itemWeight, items, n-1))
    exclude = knapSack(W, items, n-1)
    return max(include, exclude)


# items = [
#   {'id': 'a', 'val': 5, 'wt': 3},
#   {'id': 'b', 'val': 10, 'wt': 9},
#   {'id': 'c', 'val': 15, 'wt': 4},
#   {'id': 'd', 'val': 2, 'wt': 6},
#   {'id': 'e', 'val': 7, 'wt': 4}
# ]
# W = 21

# items = [
#   {'val': 60, 'wt': 10},
#   {'val': 100, 'wt': 20},
#   {'val': 120, 'wt': 30}
# ]
# W = 50
# n = len(val)
print(knapSack(W, items, n))