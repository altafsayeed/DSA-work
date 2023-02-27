def bubble_sort(my_list):                           # With each iteration, the greatest # will get sorted first, then the second highest # in the 
                                                    # next iteration, etc.
    for i in range(len(my_list) - 1, 0, -1):        # Range is length of list minus 1, go until zero, and decrement -1 with each iteration
        for j in range(i):                          # This will start at the length of the list and decrement by -1 with each iteration
            if my_list[j] > my_list[j+1]:           
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4,2,6,5,1,3]))