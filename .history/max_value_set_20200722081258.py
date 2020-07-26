
items = [
  {'id': 'a', 'val': 59, 'wt': 3000},
  {'id': 'b', 'val': 120, 'wt': 9000},
  {'id': 'c', 'val': 150, 'wt': 4000},
  {'id': 'd', 'val': 250, 'wt': 6000},
  {'id': 'e', 'val': 79, 'wt': 4000}
]
W = 21000
n = len(items)

def getMaxValueSet(W, items, n):

  if W==0 or n==0:
    return 0

  if items[n-1]['wt'] > W:
    return getMaxValueSet(W, items, n-1)
  else:
    itemValue = items[n-1]['val']
    include = (items[n-1]['val'] + getMaxValueSet(W-itemValue, items, n-1))
    exclude = getMaxValueSet(W, items, n-1)
    return max(include, exclude)

