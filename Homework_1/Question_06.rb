# Given a 2D array A[1,n][1,n] of n2 numbers such that, 
# in each row (from left to right) as well as in each column (from top to bottom), 
# the elements are in the sorted order.
# Design an O(n) time algorithm to check if A contains a given number "x". 
# Also, prove that it is not possible to design an o(n) time algorithm [i.e., a lower bound].

def search_2d(num_array, given_number)
  # Sets x at left most column, set y to last row.
  x_axis = 0
  y_axis = num_array.length - 1

  # If we go out of bound, then exit loop
  while (x_axis < num_array[y_axis].length) and (y_axis >= 0) do
    result = num_array[y_axis][x_axis]

    return "found #{result} at position X:#{x_axis + 1} Y:#{y_axis + 1}" if result == given_number
    # If current number is smaller than given number, move to next column
    # Otherwise move to lower row
    if result < given_number
      x_axis += 1
    else
      y_axis -= 1
    end  
  end
  # If we get out of bounds with rows and columns, exit loop
  return 'No answer'
end

num_array = [[1,  2,  5,	7,	12],
             [8, 	9,	10,	11,	13],
             [20, 26,	28,	31,	37],
             [21,	27,	33,	40,	56],
             [24,	29,	34,	38,	57],
             [25,	30,	37,	39,	58]]

given_number = 11

puts search_2d(num_array, given_number)