# Min Max Difference
# In this problem you will be given an array/list of integers. You need to find the largest value and the smallest value in the array. Finally you need to return the difference (largest value - smallest value) of the two values.
# Example:
# the_array = [15, 22, 84, 14, 88, 23]
# the_highest_value = 88
# the_smallest_number = 14
# the_difference = 74

numbers_list=[15, 22, 84, 14, 88, 23]
i = 0

for numbers in list(numbers_list):
    x = numbers_list[i]
    highest_num = numbers_list[i]
    lowest_num = numbers_list[i+1]
    while x > lowest_num and i < len(numbers_list):
        x = highest_num
        i = i+1
    else:
        x = lowest_num
        i = i+1
    
print ("Highest num:", highest_num)
print ("Lowest num:", lowest_num)


