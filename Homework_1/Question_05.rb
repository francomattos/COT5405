# Consider two sums, X = x1 + x2+...+xn and Y=y1+y2+...+ym. 
# Give an algorithm that finds indices i and j such that swapping xi  with yj makes the two sums equal, that is, X −xi +yj = Y −yj +xi, 
# if they exist. Analyze your algorithm.

def swap_sum(arrX, arrY, sumX, sumY)
  difference = (sumY - sumX)
  hash = {}

  arrX.each_index do |index_x|
    int_var = (2 * arrX[index_x] + difference)
    if (int_var % 2 ) == 0 then
      hash[int_var / 2] = index_x
    end
  end

  arrY.each do |y|
    if hash.has_key?(y)
      puts 'X: ' + arrX[hash[y]].to_s + ' Y: ' + y.to_s
    end
  end
end

# Case 3, simple swap
arrX = [9, 2, 8, 11, 3]
arrY = [6, 3, 5, 20, 1]
sumX = 33
sumY = 35


swap_sum(arrX, arrY, sumX, sumY)

# # Case 1, basic
# arrX = [5, 4, 7, 6, 8, 3]
# arrY = [4, 5, 9, 2, 7, 4]
# sumX = 33
# sumY = 31



# # Case 2, uneven difference
# arrX = [1, 2, 3]
# arrY = [2, 3, 4]
# sumX = 6
# sumY = 9


# # Case 3, simple swap
# arrX = [9, 2, 8, 11, 3]
# arrY = [6, 3, 5, 20, 1]
# sumX = 33
# sumY = 35

# # Case 4, no solution
# arrX = [7, 34, 8, 32]
# arrY = [1, 2, 3, 4]
# sumX = 30
# sumY = 34
