# The following question has two parts:
#   1) Your friend, John, is holding an integer array A[1,n],
#       and he tells you that the array is sorted,
#       and contains all the integers from 0 to n except one.
#       John challenges you to find the missing integer.
#       He allows you to ask him questions in the form: "What is the j-th bit of A[i]?"
#       and he is going to answer you honestly.
#       So, you can vary the values of i and j in each question you ask him.
#       Design an algorithm to find out the missing integer using O(log n) questions.
#   2) Now, John has changed the input, and the array A becomes unsorted.
#       Design an algorithm using O(n) questions to find out the missing integer.
import math
import random

# Receive the first and last index of array as top and bottom


def case_1(binary_array, bottom, top):
    # Numbers will be moving close together, until they cross around our missing number
    while top > bottom:
        # Find midpoint of bottom and top
        midpoint = math.floor((bottom + top) / 2)
        mid_bit = midpoint % 2  # Supposed bit value for least significant bit
        # Bit values same? Make bottom midpoint +1, otherwise top becomes midpoint -1
        if binary_array[midpoint][-1] == str(mid_bit):
            bottom = midpoint + 1
        else:
            top = midpoint - 1
    # After top and bottom cross, we find the midpoint of that crossing
    midpoint = round((bottom + top) / 2)
    mid_bit = midpoint % 2
    # If midpoint of crossing is same as missing bit, then it is the value after
    # otherwise it is the value before
    if binary_array[midpoint][-1] == str(mid_bit):
        result = int(binary_array[midpoint], 2) + 1
    else:
        result = int(binary_array[midpoint], 2) - 1

    return str(result)


def case_2(binary_array, bit_location):
    # Recursion until bit location is past scope
    if bit_location < 1:
        return ""
    lower = []
    higher = []
    # Starting from most significant bit, separate values matching bit 0 and 1
    for binary_val in binary_array:
        try:
            if binary_val[0 - bit_location] == "1":
                higher.append(binary_val)
            else:
                lower.append(binary_val)
        except:
            lower.append(binary_val)

    # If most significant bit have 0 values less than 2^(sigbit - 1)
    # Then missing value has that particular bit set to 0, otherwise it is 1
    # Send that array to recursion to fin what else is missing on that side
    if len(lower) == (math.pow(2, bit_location - 1)):
        binary_array = higher
        return "1" + case_2(binary_array, bit_location - 1)
    else:
        binary_array = lower
        return "0" + case_2(binary_array, bit_location - 1,)


if __name__ == "__main__":

    # Create a list of binary values
    binary_array = [format(0, "b"), format(1, "b"), format(2, "b"), format(3, "b"),
                    format(4, "b"), format(5, "b"), format(
                        6, "b"), format(7, "b"),
                    format(8, "b"), format(9, "b"), format(
                        10, "b"), format(11, "b"),
                    format(12, "b")]

    # Remove some value from list
    binary_array.remove(format(7, "b"))
    array_length = len(binary_array)

    # 1) Case where it is sorted:
    missing_number = case_1(binary_array, 0, array_length - 1)
    print(missing_number)

    # 2) Case of unsorted
    random.shuffle(binary_array)
    most_significant_bit = math.ceil(math.log(array_length, 2))

    missing_number = int(case_2(binary_array, most_significant_bit), 2)
    print(missing_number)
