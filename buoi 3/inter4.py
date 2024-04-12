def printUnorderedPairs(lstA, lstB):
    for a in lstA:
        for b in lstB:
            if a < b:
                print(f"{a},{b}")

listA = [1, 3, 5, 7]
listB = [2, 4, 6, 8]
printUnorderedPairs(listA, listB)