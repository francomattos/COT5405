/*
Define maximum partial sum problem (MPS) as follows. Given an array A[1,n] of integers, 
and values of i and j with 1≤i ≤j≤n such that A[i]+A[i+1]+A[i+2]+...+A[j] is maximized. 
For example, for the array [3,-5,6,7,8,-10,7], the solution to MPS is i = 3 and j = 5 (sum is 21). 
Design an O(n log n) time algorithm. [Hint: Divide and Conquer approach]. Can you improve the time complexity to O(n). 
*/

const maximum_partial_sum = (array_values) => {
  // Result object, to keep track of values
  let result = {
    i: 0,
    j: 0,
    max_partial_sum: array_values[0],
  };

  // Sets current sum to first value.
  let running_sum = array_values[0];
  let curr_i = 0;

  for (let j = 1; j < array_values.length; j++) {
    let current_value = array_values[j];
    // Case where current value is greater than previous sum and the max sum.
    if (
      current_value > running_sum + current_value &&
      current_value >= result.max_partial_sum
    ) {
      result = {
        i: j,
        j: j,
        max_partial_sum: current_value,
      };
      // We reset the i index to current index and skip any other checks.
      curr_i = j;
      running_sum = current_value;
      continue;
    }
    // Case where adding current value increases the current running sum.
    if (running_sum + current_value > result.max_partial_sum) {
      // We just update result.
      result = {
        i: curr_i,
        j: j,
        max_partial_sum: running_sum + current_value,
      };
    }
    running_sum += current_value;
    // Case where adding current value makes running sum negative.
    if (running_sum < 0 && current_value < running_sum) {
      // We reset.
      curr_i = j + 1;
      running_sum = 0;
    }
  }
  return result;
};

some_array = [-1, -3, -2, -20, 5, 4, -10, 8, 15, 5, 6, 35];

console.log(maximum_partial_sum(some_array));
