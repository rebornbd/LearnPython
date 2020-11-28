'''
count()     index()
'''

def main():
    t = (1, 2, 3, 4, 3)

    t.count(3)      # 2
    t.index(3)      # 2

    for i in t:
        print(i)


main()
