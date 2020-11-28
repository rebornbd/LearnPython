'''
False   await	    else	    import	    pass
None	break	    except	    in	        raise
True	class	    finally     is	        return
and	    continue	for	        lambda	    try
as	    def	        from	    nonlocal	while
assert	del	        global	    not	        with
async	elif	    if	        or	        yield
'''

import math
from math import sqrt

def keywords():
    flag = True and False
    flag = not True # False
    print(flag)

def div():
    a = 11
    b = 0.0

    try:
        d = a/b
    except Exception as e:
        print(e)

def loop():
    for i in range(0, 10):
        print(i)
    
    i = 0
    while(i < 10):
        print(i)
        i += 1

def sqrt_import():
    num1 = 21

    s1 = math.sqrt(num1) # import math
    s2 = sqrt(num1)      # from math import sqrt

    print("math.sqrt(%s): %s" % (num1, s1))
    print("     sqrt(%s): %s" % (num1, s2))


sqrt_import()
div()
keywords()
