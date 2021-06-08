import sys

def removedupnew(sortedlist:list):
    if sortedlist is None:
        return
    if len(sortedlist) < 1:
        return
    new_sortedlist = []
    for elem in sortedlist:
        if elem not in new_sortedlist:
            new_sortedlist.append(elem)
    return new_sortedlist

def removedupself(sortedlist:list):
    if sortedlist is None:
        return
    if len(sortedlist) < 1:
        return
    slow,fast = 0,0
    while fast < len(sortedlist):
        if sortedlist[slow]!=sortedlist[fast]:
            slow += 1
            sortedlist[slow] = sortedlist[fast]
        fast += 1
    return slow+1, sortedlist[0:slow:1]


if __name__ == '__main__':
    for line in sys.stdin:
        lines = line.split()
        #print(removedupnew(lines[0]))
        #print(removedupself(lines[0]))