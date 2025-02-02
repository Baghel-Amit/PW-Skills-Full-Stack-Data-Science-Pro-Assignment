#!/usr/bin/env python
# coding: utf-8

# #                                            Time Complexity + Recursion
# 

#  Find time complexity of below code blocks :
# 

# Problem 1 :
# 
# def quicksort(arr):
# 
# if len(arr) <= 1: 
# 
# return arr
# 
# pivot = arr[len(arr) // 2]
# 
# left = [x for x in arr if x < pivot]
# 
# middle = [x for x in arr if x == pivot]
# 
# right = [x for x in arr if x > pivot]
# 
# return quicksort(left) + middle + quicksort(right)
# 

# SOL.
# The time complexity of the given QuickSort function depends on how the pivot is chosen and how the array is partitioned. Let's analyze it:
# 
# Best and Average Case Complexity: O(nlogn)O(n \log n)O(nlogn)
#     
# •	If the pivot chosen is approximately the median, the array is evenly divided into two equal halves.
# •	The recurrence relation for the time complexity is: T(n)=2T(n/2)+O(n)T(n) = 2T(n/2) + O(n)T(n)=2T(n/2)+O(n)
# o	The O(n)O(n)O(n) term comes from the partitioning step (creating left, middle, and right).
# o	Solving this recurrence using the Master Theorem gives: O(nlog⁡n)O(n \log n)O(nlogn)
#     
# Worst Case Complexity: O(n2)O(n^2)O(n2)
#     
# •	If the pivot is always the smallest or largest element, the array is divided into one part of size n−1n-1n−1 and another of size 0.
# •	The recurrence relation becomes: T(n)=T(n−1)+O(n)T(n) = T(n-1) + O(n)T(n)=T(n−1)+O(n)
# •	This simplifies to: O(n2)O(n^2)O(n2)
# •	This occurs when sorting an already sorted array (ascending or descending) if the pivot is poorly chosen.
# 
# Space Complexity: O(n)O(n)O(n)
#     
# •	Since Python lists are immutable, list comprehensions create new lists (left, middle, right), leading to an extra O(n)O(n)O(n) space.
# Final Answer:
# •	Best/Average Case: O(nlogn)O(n \log n)O(nlogn)
# •	Worst Case: O(n2)O(n^2)O(n2)
# •	Space Complexity: O(n)O(n)O(n)
# 

# Problem 2 :
#     
# def nested_loop_example(matrix):
#     
# rows, cols = len(matrix), len(matrix[0])
# 
# total = 0
# 
# for i in range(rows):
#     
# for j in range(cols):
#     
# total += matrix[i][j]
# 
# return total
# 

# SOL.
# 
# Time Complexity Analysis:
# 
# The function iterates through every element of the given matrix. Let's break it down:
# 
# 1.	rows, cols = len(matrix), len(matrix[0]) → O(1)O(1)O(1)
# 
#     o	Extracting the number of rows and columns takes constant time.
# 
# 2.	Nested Loops:
# 
#     o	The outer loop runs rowsrowsrows times.
# 
#     o	The inner loop runs colscolscols times for each row.
#     o	So, the total number of iterations is rows×colsrows \times colsrows×cols.
#     
# 3.	Inside the inner loop, the operation total += matrix[i][j] takes O(1)O(1)O(1) time.
# 
# Thus, the total time complexity is:
# O(rows×cols)=O(n×m)O(\text{rows} \times \text{cols}) = O(n \times m)O(rows×cols)=O(n×m)
# where nnn is the number of rows and mmm is the number of columns.
# 
# Space Complexity:
# •	The function only uses a few extra variables (rows, cols, total), which takes O(1)O(1)O(1) space.
# •	No additional data structures are used.
# 
# Final Answer:
# •	Time Complexity: O(n×m)O(n \times m)O(n×m) (where nnn is the number of rows and mmm is the number of columns)
# •	Space Complexity: O(1)O(1)O(1)

# Problem 3 :
#     
# def example_function(arr):
#     
# result = 0
# 
# for element in arr:
#     
# result += element
# 
# return result

#  Sol.
#  
# The function iterates through every element in the input list arr once.
# 
# 1.	Loop Iteration:
# 
#    o	The for loop runs nnn times, where nnn is the length of arr.
#    o	The operation result += element inside the loop runs in O(1)O(1)O(1) time.
#    
# Thus, the total time complexity is:
# O(n)O(n)O(n)
# 
# Space Complexity Analysis:
# 
#    •	The function uses only a few extra variables (result and element), which take O(1)O(1)O(1) space.
#    •	No additional data structures are used.
#    
# Final Answer:
#    •	Time Complexity: O(n)O(n)O(n) (linear time)
#    •	Space Complexity: O(1)O(1)O(1) (constant space)
# 

# Problem 4 :
#     
# def longest_increasing_subsequence(nums):
#     
# n = len(nums)
# 
# lis = [1] * n
# 
# for i in range(1, n):
#     
# for j in range(0, i):
#     
# if nums[i] > nums[j] and lis[i] < lis[j] + 1:
#     
# lis[i] = lis[j] + 1
# 
# return max(lis)
# 
# 

# SOL.
# Time Complexity Analysis:
# 
# The function calculates the Longest Increasing Subsequence (LIS) using Dynamic Programming with a nested loop approach.
#    1.Outer loop (for i in range(1, n)):
#        o	Runs n−1n-1n−1 times (approximately O(n)O(n)O(n)).
#   2.Inner loop (for j in range(0, i)):
#        o	In the worst case, j iterates up to i-1, leading to a total number of comparisons as: 1+2+3+...+(n−1)=n(n−1)21 + 2             + 3 + ... + (n-1) = \frac{n(n-1)}{2}1+2+3+...+(n−1)=2n(n−1)
#        o	This simplifies to O(n2)O(n^2)O(n2).
#        
# Thus, the overall time complexity of this function is O(n2)O(n^2)O(n2).
# 
# Space Complexity Analysis:
# 
# •	The function uses an extra list lis of size n, leading to O(n)O(n)O(n) space complexity.
# •	Other variables (n, i, j) use O(1)O(1)O(1) space.
# 
# Thus, the overall space complexity is O(n)O(n)O(n).
# 
# Final Answer:
# •	Time Complexity: O(n2)O(n^2)O(n2) (quadratic time)
# •	Space Complexity: O(n)O(n)O(n) (linear space)
# 

# Problem 5 :
#     
# def mysterious_function(arr):
#     
# n = len(arr)
# 
# result = 0
# 
# 
# for i in range(n):
#     
# for j in range(i, n):
#     
# result += arr[i] * arr[j]
# 
# return result
# 
# 
# 

# Time Complexity Analysis:
# 
# The function contains a nested loop, where:
# 
#    1.Outer loop (for i in range(n)):
#          o	Runs O(n)O(n)O(n) times.
#   2.Inner loop (for j in range(i, n)):
#          o	The value of j starts from i and goes up to n-1, leading to the following iterations: (n−i) times for each i(n - i)             \text{ times for each } i(n−i) times for each i
#          o	The total number of iterations across all loops is: ∑i=0n−1(n−i)=n+(n−1)+(n−2)+...+1\sum_{i=0}^{n-1} (n - i) = n +             (n-1) + (n-2) + ... + 1i=0∑n−1(n−i)=n+(n−1)+(n−2)+...+1
#          o	This forms an arithmetic series summing to: n(n+1)2\frac{n(n+1)}{2}2n(n+1)
#          o	This simplifies to O(n2)O(n^2)O(n2).
#          
#  Thus, the overall time complexity is O(n2)O(n^2)O(n2).
#  
# Space Complexity Analysis:
# 
# •	The function only uses a few integer variables (n, result, i, j).
# •	No extra data structures are used.
# Thus, the space complexity is O(1)O(1)O(1) (constant space).
# 
# Final Answer:
# •	Time Complexity: O(n2)O(n^2)O(n2) (quadratic time)
# •	Space Complexity: O(1)O(1)O(1) (constant space)
# 

# 
# # Solve the following problems on recursion

# Problem 6 : Sum of Digits
# 
# Write a recursive function to calculate the sum of digits of a given positive integer.
# 
# sum_of_digits(123) -> 6
# 
# Recursive Function for Sum of Digits
# 
# The function should:
#  1.	Extract the last digit using n % 10.
#  2.	Reduce the number by removing the last digit using n // 10.
#  3.	Recursively call itself until n becomes 0.
# ________________________________________
# 
# Implementation:
# python
# CopyEdit
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_of_digits(n // 10)
# 
# # Example Usage:
# 
# print(sum_of_digits(123))  # Output: 6
# 
# Time Complexity Analysis:
# 
#    •	The function reduces n by a factor of 10 in each recursive call.
#    •	The number of recursive calls is equal to the number of digits in n, which is O(log⁡n)O(\log n)O(logn) (since n has approximately log10(n) digits).
#    
# Space Complexity Analysis:
# 
#    •	The function uses O(log⁡n)O(\log n)O(logn) space due to recursive calls on the call stack.
# Final Complexity:
# 
#    •	Time Complexity: O(log⁡n)O(\log n)O(logn)
#    
#    •	Space Complexity: O(log⁡n)O(\log n)O(logn)
# 

# In[13]:


Problem 7: Fibonacci Series

Write a recursive function to generate the first n numbers of the Fibonacci series.

fibonacci_series(6) -> [0, 1, 1, 2, 3, 5]


# In[14]:


def fibonacci_series(n, series=None):

   if series is None:
   
       series = [0, 1]  # Start the series with the first two Fibonacci numbers.
   
   # Base condition to stop recursion when the length of the series reaches n
   if len(series) >= n:
       return series[:n]
   
   # Recursive case: calculate the next Fibonacci number and append it
   series.append(series[-1] + series[-2])
   return fibonacci_series(n, series)

# Test the function

print(fibonacci_series(6))   


# Problem 8 : Subset Sum
#     
# Given a set of positive integers and a target sum, write a recursive function to determine if there exists a subset
# 
# of the integers that adds up to the target sum.
# 
# subset_sum([3, 34, 4, 12, 5, 2], 9) -> True
# 

# In[9]:


def subset_sum(nums, target_sum):
    # Base cases
    if target_sum == 0:  # If the target sum is 0, we can achieve it by choosing no elements
        return True
    if not nums:  # If no elements left, and target sum is not 0
        return False
    
    # Recursive case: include the current element or exclude it
    current_num = nums[0]
    
    # Check if target sum can be achieved by either including or excluding the current number
    return subset_sum(nums[1:], target_sum) or subset_sum(nums[1:], target_sum - current_num)

# Test the function
print(subset_sum([3, 34, 4, 12, 5, 2], 9))  # Output: True


# Problem 9: 
# Word Break Given a non-empty string and a dictionary of words, write a recursive function to determine if the string can be segmented into a space-separated sequence of dictionary words. word_break( leetcode , [ leet , code ]) -> True
# 

# In[10]:


def word_break(s, word_dict):
    # Base case: if the string is empty, return True
    if not s:
        return True
    
    # Try every possible prefix of the string
    for word in word_dict:
        # If the string starts with the current word, recursively check the remainder of the string
        if s.startswith(word):
            if word_break(s[len(word):], word_dict):
                return True
    
    # If no valid segmentation is found, return False
    return False

# Test the function
print(word_break("leetcode", ["leet", "code"]))  # Output: True


# Problem 10 : N-Queens
# 
# Implement a recursive function to solve the N Queens problem, where you have to place N queens on an N×N
# 
# chessboard in such a way that no two queens threaten each other.
# 
# n_queens(4)
# 
# [
# [".Q..",
# "...Q",
# "Q...",
# "..Q."],
# ["..Q.",
# "Q...",
# "...Q",
# ".Q.."]
# 

# In[11]:


def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False
    
    return True

def n_queens(n):
    def solve(board, row):
        # Base case: If all queens are placed
        if row == n:
            solution = [''.join(row) for row in board]
            result.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'  # Place queen
                solve(board, row + 1)  # Recur to place queen in next row
                board[row][col] = '.'  # Backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]  # Create empty chessboard
    solve(board, 0)  # Start solving from the first row
    return result

# Test the function
solutions = n_queens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()  # Add an empty line between solutions


# In[ ]:




