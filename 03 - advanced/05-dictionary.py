'''
clear()                         get()
copy()          items()         setdefault()
pop()           keys()          update()
popitem()       values()        fromkeys()



clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

def main():
    d = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

    d.items()       # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
    d.keys()        # dict_keys(['key1', 'key2', 'key3'])
    d.values()      # dict_values(['value1', 'value2', 'value3'])

    d1 = d.copy()       # seperate copy of d
    rv = d1.popitem()   # removes and returns the (key, value) pair in LIFO order | rv = ('key3', 'value3'), d1 = {'key1': 'value1', 'key2': 'value2'}


main()
