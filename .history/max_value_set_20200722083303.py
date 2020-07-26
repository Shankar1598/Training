
items = [
  {'id': 'a', 'val': 59, 'wt': 3000},
  {'id': 'b', 'val': 120, 'wt': 9000},
  {'id': 'c', 'val': 150, 'wt': 4000},
  {'id': 'd', 'val': 250, 'wt': 6000},
  {'id': 'e', 'val': 79, 'wt': 4000}
]
W = 21000
n = len(items)

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


items = [
  {'val': 60, 'wt': 10},
  {'val': 100, 'wt': 20},
  {'val': 120, 'wt': 30},
  {'val': 220, 'wt': 10}
]
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(items)
print(knapSack(W, items, n))
print(items)