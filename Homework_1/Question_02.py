# Given an array A[1,n] of n numbers, compute the k-th smallest element in A for k=1,2,4,8,16,32 ...
# (i.e.  all power of 2 up to n) in total time O(n).

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
    index = 0
    medians = []

    # Gets the middle value out of blocks of 5
    while index + 5 < len(array_values):
        temp_array = array_values[index:index + 5]
        temp_array.sort()
        medians.append(temp_array[2])
        index += 5
    # Returns the middle value of all the batches
    return medians[math.floor(len(medians)/2)]


if __name__ == "__main__":
    # randomized list of a sequence of 50 integers
    number_array = [5, 2, 8, 4, 1, 6, 7, 3, 9, 19, 15, 11, 12, 18, 14, 20, 16]

    # Finds largest exponent that fits into number of n value
    largest_exponent = math.floor(math.log(len(number_array), 2))

    # generate kth values array
    kth_values = []

    for exponent in range(largest_exponent + 1):
        kth_values.append(round(math.pow(2, exponent)))

    result = select_element(number_array, kth_values)
    result.sort()

    print(f"The kth values are: {result}")
