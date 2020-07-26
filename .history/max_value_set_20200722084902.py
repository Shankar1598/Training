
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
  {'val': 120, 'wt': 30}
]
W = 50
n = len(items)
print(knapSack(W, items, n))