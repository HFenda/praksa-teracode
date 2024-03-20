"""
Task

You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format

A single line of input containing  space separated integers.

Output Format

Print the 3X3 NumPy array.

Sample Input
1 2 3 4 5 6 7 8 9
Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
import numpy

int_list = numpy.array(list(map(int, input().split())))
int_list=numpy.reshape(int_list,(3,3))
print(int_list)
