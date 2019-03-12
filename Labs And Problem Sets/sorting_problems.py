# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below.  Print the new list.

my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
my_list[2], my_list[7] = my_list[7], my_list[2]
print(my_list)

# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.

sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]

def selection_sort(my_list):
    selection_big_loop = 0
    selection_small_loop = 0
    for  current_pos in range(len(my_list)):
        selection_big_loop += 1
        minimum_pos = current_pos
        for scan_pos in range(current_pos + 1, len(my_list)):
            selection_small_loop += 1
            if my_list[scan_pos] < my_list[minimum_pos]:
                minimum_pos = scan_pos
        my_list[current_pos], my_list[minimum_pos] = my_list[minimum_pos], my_list[current_pos]
    print("times through the big loop during selection sort: ", selection_big_loop)
    print("times through the small loop during selection sort: ", selection_small_loop)
selection_sort(sort_me)
print("selection sort: ", sort_me)


# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]
def insertion_sort(my_list):
    big_loop = 0
    small_loop = 0
    for key_pos in range(1, len(my_list)):
        big_loop += 1
        key_val = my_list[key_pos]
        scan_pos = key_pos - 1  # look to list item on the left
        while scan_pos >= 0 and my_list[scan_pos] > key_val:
            small_loop += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1
        my_list[scan_pos + 1] = key_val
    print("times through the big loop during insertion sort: ", big_loop)
    print("times through the small loop during insertion sort: ", small_loop)
insertion_sort(sort_me2)
print("insertion sort: ", sort_me2)

# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.  Ask if you have questions.
# Make the functions print each value (times through big loop and inner loop).  
# Run each sort on the list below with the results of the efficiency (loop counts) printed.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]
selection_sort(sort_me3)
insertion_sort(sort_me3)
print(sort_me3)