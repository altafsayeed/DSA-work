# In 2 hash tables, determine whether the 2 lists have any items in common

def item_in_common(list1, list2):       # Naive Approach, O(n^2)
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def item_in_common2(list1, list2):      # Efficient approach, O(n)
    mydict = {}
    for i in list1:
        mydict[i] = True

    for j in list2:
        if j in mydict:
            return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common2(list1, list2))