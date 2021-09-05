# Given an array A[1,n] of n numbers, compute the k-th smallest element in A for k=1,2,4,8,16,32 ... (i.e.  all power of 2 up to n) in total time O(n). 

import math

def select_element(number_array, kth_values):
    result = []
    # If the list is smaller than 5, just sort and return value corresponding to index.
    if len(number_array) <= 5:
        number_array.sort()  # Trivial cost compared to n
        for index in kth_values:
            result.append(number_array[index - 1])
        return result

    median = get_median_of_medians(number_array)
    array_small = []
    array_large = []
    # Creates two arrays with pivot point as median. Does not add median to array
    for value in number_array:
        if value < median:
            array_small.append(value)
        elif value > median:
            array_large.append(value)

    large_kth_values = []
    # Iterates descending through kth values while they are smaller than the length of small array
    while kth_values and len(array_small) < kth_values[-1]:
        # If median is in kth position, add it to result
        if len(array_small) + 1 == kth_values[-1]:
            kth_values.pop()
            result.append(median)
        else:
            # We are discarting median, so we create large_kth_values array subtracting array small + 1 to account for median
            large_kth_values.insert(
                0, kth_values.pop() - (len(array_small) + 1))

    # Recursive call for large and small array.
    if kth_values:
        result += select_element(array_small, kth_values)
    if large_kth_values:
        result += select_element(array_large, large_kth_values)

    return result

# Function to create median of medians


def get_median_of_medians(array_values):
    median_point = 2
    medians = []
    # Gets the middle value out of blocks of 5
    while median_point < len(array_values):
        medians.append(array_values[median_point])
        median_point += 5
    # Returns the middle value of all the batches
    return medians[math.floor(len(medians)/2)]


if __name__ == "__main__":
    # randomized list of a sequence of 50 integers
    number_array = [1, 2, 3, 4, 5, 6, 7, 8]

    # Finds largest exponent that fits into number of n value
    largest_exponent = math.floor(math.log(len(number_array), 2))

    # generate kth values array
    kth_values = []
    for exponent in range(largest_exponent + 1):
        kth_values.append(round(math.pow(2, exponent)))

    print(select_element(number_array, kth_values))
