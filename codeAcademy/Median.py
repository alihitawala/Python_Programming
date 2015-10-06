__author__ = 'aliHitawala'
def median(lis):
    length = len(lis)
    lis = sorted(lis)
    med = 0
    mid = length /2
    if (length %2 == 0):
        med = (lis[mid]+lis[mid-1]) / 2.0
    else:
        med = lis[mid]
    return med

print median([5,4,4,5])