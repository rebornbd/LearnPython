'''
python loops
------------
with: continue, break
'''

def main():
    for i in range(1, 10):
        if (i == 5):
            continue

        if (i == 7):
            break
        print(i, end=' ')
    print()
    
    i = 0
    while(i < 10):
        i += 1
        if (i == 5):
            continue

        if (i == 7):
            break
        print(i, end=" ")
    print()

# -------
main()
