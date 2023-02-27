def selection_sort(my_list):
    for i in range(len(my_list)-1):                 # Start at index 0 and end at last index of list
        min_index = i                               # Set min index to first index of list
        for j in range(i+1, len(my_list)):          # Use j for num we will compare to, start at i+1
            if my_list[j] < my_list[min_index]:     # Once we find an item less than the current min index, set min index to that item
                min_index = j
        if i != min_index:                          # If there is a new min index, switch the old min index value with new one
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list
    
print(selection_sort([4,2,6,5,1,3]))