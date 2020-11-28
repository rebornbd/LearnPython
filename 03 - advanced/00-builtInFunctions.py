'''
abs()           delattr()       hash()          memoryview()    set()
all()           dict()          help()          min()           setattr()
any()           dir()           hex()           next()          slice()
ascii()         divmod()        id()            object()        sorted()
bin()           enumerate()     input()         oct()           staticmethod()
bool()          eval()          int()           open()          str()
breakpoint()    exec()          isinstance()    ord()           sum()
bytearray()     filter()        issubclass()    pow()           super()
bytes()         float()         iter()          print()         tuple()
callable()      format()        len()           property()      type()
chr()           frozenset()     list()          range()         vars()
classmethod()   getattr()       locals()        repr()          zip()
compile()       globals()       map()           reversed()      __import__()
complex()       hasattr()       max()           round()
'''

def main():
    l = list([5, 4, 3, 2, 1])

    min(l)      # 1
    max(l)      # 5

    sorted(l)   # [1, 2, 3, 4, 5]
    

main()
