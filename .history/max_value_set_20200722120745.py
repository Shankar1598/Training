

def knapSack(W, items, n):

  if (n == 0 or W==0):
    return 0
  
  itemValue = items[n-1]['val']
  itemWt = items[n-1]['wt']

  if (itemWt > W):
    return knapSack(W, items, n-1)
  else:
    # include nth item
    included = (itemValue + knapSack(W-itemWt, items, n-1))
    # exclude nth item
    excluded = knapSack(W, items, n-1)

    result = max(included, excluded)
    return result









# items = [
#   {'val': 60, 'wt': 10},
#   {'val': 100, 'wt': 20},
#   {'val': 120, 'wt': 30}
# ]
# W = 50

items = [
  {'id': 'a', 'val': 5, 'wt': 3},
  {'id': 'b', 'val': 10, 'wt': 9},
  {'id': 'c', 'val': 15, 'wt': 4},
  {'id': 'd', 'val': 2, 'wt': 6},
  {'id': 'e', 'val': 7, 'wt': 4}
]
W = 21

n = len(items)
print(knapSack(W, items, n))

