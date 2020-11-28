'''
append()        extend()        insert()        remove()        pop()
clear()         index()         count()         sort()          reverse()
copy()
'''

def main():
    l = [5, 4, 3, 2, 1]

    l.append(6)         # [5, 4, 3, 2, 1, 6]
    l.insert(0, 7)      # [7, 5, 4, 3, 2, 1, 6]

    l.remove(7)         # [5, 4, 3, 2, 1, 6]
    l.pop()             # [5, 4, 3, 2, 1]

    l.sort()            # [1, 2, 3, 4, 5]
    l.reverse()         # [5, 4, 3, 2, 1]

    l1 = l              # reference copy
    l1 = l.copy()       # separate  copy

    # reference copy problems
    l1 = [1, 2, 3]
    l2 = l1
    l2.append(4)
    print(l2)       # [1, 2, 3, 4]
    print(l1)       # [1, 2, 3, 4] | because it's same reference
    # separate  copy
    l1 = [1, 2, 3]
    l2 = l1.copy()
    l2.append(4)
    print(l2)       # [1, 2, 3, 4]
    print(l1)       # [1, 2, 3] | not update l1, because it's diff/separe copy

    l1 = [1, 2, 3]
    l2 = [4, 5]
    l1.extend(l2)
    print(l1)       # [1, 2, 3, 4, 5]

    l.sort()        # [1, 2, 3, 4, 5]
    l.index(3)      # 2
    l.count(4)      # 1
    
    l.clear()       # []


main()
