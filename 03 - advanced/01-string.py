'''
capitalize()    casefold()      center()        count()         encode()        endswith()
expandtabs()    find()          format()        index()         isalnum()       format_map()
isalpha()       isascii()       isdecimal()     isdigit()       islower()       isidentifier()
isnumeric()     isspace()       istitle()       isupper()       join()          ljust()
isprintable()   lower()         lstrip()        maketrans()     partition()     replace()
rfind()         rindex()        rjust()         rpartition()    rsplit()        rstrip()
split()         splitlines()    startswith()    strip()         swapcase()      title()
translate()     upper()         zfill()


# importants methods
--------------------
capitalize()    count()         split()         join()
lower()         find()          strip()
upper()         startswith()    lstrip()
islower()       endswith()      rstrip()
isupper()       isspace()       replace()
'''

def main():
    s  = 'this is a simple test'
    ss = "  aa bb  "

    s.capitalize()      # 'This is a simple test'
    s.lower()           # 'this is a simple test'
    s.upper()           # 'THIS IS A SIMPLE TEST'

    s.islower()         # True
    s.isupper()         # False

    s.startswith('th')  # True
    s.endswith('test')  # True
    s.isspace()         # False, [' \n \t'.isspace()] -> True || true, if it's only contains whitespace

    s.count('is')       # 2
    s.find('test')      # 17

    s.split()           # ['this', 'is', 'a', 'simple', 'test']
    ss.strip()          # "aa bb"

    ", ".join(['aa', 'bb'])     # "aa, bb"
    s.replace('this', 'This')   # 'This is a simple test'


main()
