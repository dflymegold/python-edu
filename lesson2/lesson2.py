# Sort list by second element
def sortbysecondelement(list):
    sortedlist = sorted(list, key=lambda k: k[1])
    return sortedlist
# Make dictionary from sorted list
def makedictionary(sortedlist):
    dictionary = {el.pop(1): el for el in sortedlist}
    return dictionary
# Sort Dictionary value by descending
def sortvaluesasc (dictionary):
    res = {k: sorted(v, reverse=True) for k, v in dictionary.items()}
    return res
# Get set from all values of dictionary
def getset (changeddictionary):
    values = list(changeddictionary.values())
    my_set = set(map(tuple, values))
    return my_set
# Convert set to string
def settostring (my_set):
    my_string = str(my_set)
    return my_string
def main ():
    alist = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
    sorted = sortbysecondelement(alist)
    print(sorted)
    adictionary = makedictionary(sorted)
    print(adictionary)
    sorteddictionary = sortvaluesasc(adictionary)
    print (sorteddictionary)
    valueset = getset(sorteddictionary)
    print (valueset)
    valuestring = settostring(valueset)
    print (valuestring)
    print (type(valuestring))

if __name__ == '__main__':
    main()