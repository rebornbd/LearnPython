'''
add()           discard()       difference()            symmetric_difference()
update()        copy()          difference_update()     symmetric_difference_update()
remove()        clear()         intersection()
pop()           union()         intersection_update()

isdisjoint()    issubset()      issuperset()
'''

def main():
    s = {1, 2, 3}
    l = [4, 5]

    s.add(4)        # {1, 2, 3, 4}
    s.update(l)     # {1, 2, 3, 4, 5} | s.update(iterable)

    s.remove(5)     # {1, 2, 3, 4}  | if found then remove, else get an Exception
    s.discard(4)    # {1, 2, 3}     | if found then remove, else nothing
    s.pop()         # {2, 3}        | pop/delete first insert elements

    a = {1, 2, 3, 4, 5, 6, 7, 8}
    b = {1, 3, 5, 7}
    c = {2, 4, 6, 8}

    # difference: (-)
    d = a.difference(b)         # {2, 4, 6, 8}
    d = a-b                     # {2, 4, 6, 8}
    A = a.copy()                # seperate copy of a
    A.difference_update(b)      # A = {2, 4, 6, 8} | result is assigned to A

    # intersection: (∩ -> &)
    i = a.intersection(b)       # {1, 3, 5, 7}
    i = a & b                   # {1, 3, 5, 7}
    A = a.copy()                # seperate copy of a
    A.intersection_update(b)    # A = {1, 3, 5, 7} | result is assigned to A

    # union: (∪ -> |)
    u = a.union(b)          # {1, 2, 3, 4, 5, 6, 7, 8}
    u = a | b               # {1, 2, 3, 4, 5, 6, 7, 8}

    # symmetric_difference: (^) | A^B = (A|B) - (A&B)
    A = {1, 2, 5, 7}
    B = {0, 2, 5, 8}
    sd = A.symmetric_difference(B)      # sd = {0, 1, 7, 8}
    sd = A ^ B                          # sd = {0, 1, 7, 8}
    A.symmetric_difference_update(B)    #  A = {0, 1, 7, 8}

    a = {1, 2, 3, 4, 5, 6}
    b = {2, 4, 6}
    c = {7, 8, 9}

    # disjoint
    a.isdisjoint(b)         # False
    a.isdisjoint(c)         # True | a ∩ c = ∅, so that a & c is disjoint

    # subset: B.issubset(A) | B is a subset of A
    b.issubset(a)           # True | if set b all elements are in set a, then b is a subset of a
    a.issubset(b)           # False
    c.issubset(a)           # False

    # superset: A.issuperset(B) | A is a superset of B
    a.issubset(b)           # True


main()
