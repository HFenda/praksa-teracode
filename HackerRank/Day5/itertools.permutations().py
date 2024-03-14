"""
Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string S and the integer value k.
Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

from itertools import permutations
string,k=input().split()

permutation_list=list(permutations(string,int(k)))
joined_permutation_list=["".join(element) for element in permutation_list]
sorted_list=sorted(joined_permutation_list)
print(*(i for i in sorted_list),sep='\n')
