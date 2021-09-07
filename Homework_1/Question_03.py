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


def case_1(binary_array, array_length):
    if array_length == 2:
        if binary_array[0][-1] == binary_array[1][-1]:
            missing_number = int(binary_array[0], 2) + 1
            print(f"missing number is {missing_number}")
            return 0

    midpoint = math.floor(array_length / 2)
    mid_bit = midpoint % 2
    print(f"midpoint {midpoint}")
    print(f"mid_bit {mid_bit}")
    print(f"binary_array[midpoint][-1] {binary_array[midpoint][-1]}")

    if binary_array[midpoint][-1] == str(mid_bit):
        print("Side: right")
        binary_array = binary_array[midpoint + 1:]
        array_length = len(binary_array)
        print(f"binary_array {binary_array}")
        if array_length == 1:
            result = int(binary_array[0], 2) + 1
            print(result)
            return 0
    else:
        print("Side: left")
        binary_array = binary_array[:midpoint]
        array_length = len(binary_array)
        print(f"binary_array {binary_array}")
        if array_length == 1:
            result = int(binary_array[0], 2) - 1
            print(result)
            return 0

    return case_1(binary_array, array_length)


def case_2(binary_array, array_length):
    pass


if __name__ == "__main__":

    # Create a list of binary values
    binary_array = [format(0, "b"), format(1, "b"), format(2, "b"), format(3, "b"),
                    format(4, "b"), format(5, "b"), format(
                        6, "b"), format(7, "b"),
                    format(8, "b"), format(9, "b"), format(10, "b")]

    # Remove some value from list
    binary_array.remove(format(7, "b"))
    array_length = len(binary_array)

    # 1) Case where it is sorted:
    result = case_1(binary_array, array_length)

    # 2) Case of unsorted
    # Format makes a binary string in python where the most significant bit is always 1
    # Except for the case of 0
    # We can use to check the most significant bit by means of length of the string
    random.shuffle(binary_array)
    most_significant_bit = math.ceil(math.log(array_length, 2))
