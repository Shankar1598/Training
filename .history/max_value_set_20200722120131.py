

def knapSack(W, items, n):

  if (n == 0 or W==0):
    return 0
  
  itemValue = items[n-1]['val']
  itemWt = items[n-1]['wt']

  if (itemWt > W)









items = [
  {'val': 60, 'wt': 10},
  {'val': 100, 'wt': 20},
  {'val': 120, 'wt': 30}
]
W = 50
n = len(items)
# print(knapSack(W, items, n))

