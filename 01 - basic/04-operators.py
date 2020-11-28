'''
python operators
----------------
arithmetic: [+  -  *  /  %  **  //]
comparison: [==  !=  >  >=  <  <=]
bitwise:    [&  |  ~  ^  <<  >>]
assignment: [=  +=  -=  *=  /=  %=  **=  //=  &=  |=  ~=  ^=  >>=  <<=]
logical:    [and  or  not]
membership: [(in) (not in)]
identity:   [(is)  (is not)]

NB: **(exponent) | //(floorDivision) | ^(xor) | ~(bitwise not) | <<(left shift) | >>(right shift)
'''

def main():
    a = 11
    b = 2.0
    myList = [1, 2, 3, 4]

    aExp = a**4

    isInList = 4 in myList # True
    isInList = 5 not in myList # True

    # == is for: value equality
    # is is for: reference equality

    # mutable [], {}
    mf = [] == [] # True
    mf = [] is [] # False

    # immutable (), ''
    imf = () == () # True
    imf = () is () # True


main()
