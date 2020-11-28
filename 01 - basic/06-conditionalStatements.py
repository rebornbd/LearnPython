'''
conditional statements
----------------------

if (con):
    # something
elif (con):
    # something
else:
    # something
'''

def main():
    num = 25

    if (num<20):
        print("%s is smaller than 20" % (num))
    elif(num < 30):
        print("%s is smaller than 30" % (num))
    else:
        print("%s is greater than or equal to 30" % (num))

main()
