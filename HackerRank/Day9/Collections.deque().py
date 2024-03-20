"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque d.

Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output
1 2
"""
from collections import deque

d = deque()
n = int(input())

for i in range(n):
    order_list = input().split()
    if len(order_list) > 1:
        order, value = order_list[0], order_list[1]
    else:
        order = order_list[0]
        value = None

    if value is not None:
        getattr(d, order)(value)
    else:
        getattr(d, order)()

print(*d)