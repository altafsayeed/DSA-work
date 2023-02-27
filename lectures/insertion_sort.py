def insertion_sort(my_list):
    for i in range(1, len(my_list)):    # Start at second item in the list
        temp = my_list[i]               # Create temp var and set it to second item
        j = i - 1                       # Create variable for item before temp called j
        while temp < my_list[j] and j > -1:     # While temp is less than item before it and while j is not going past the first element
            my_list[j + 1] = my_list[j]         # Switch the numbers
            my_list[j] = temp                   
            j -= 1                          # Decrement j by 1 and run while loop again to check prior numbers in list
    return my_list

print(insertion_sort([4,2,6,5,1,3]))