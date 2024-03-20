"""
Task

You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format
A single line containing the string S and integer value k separated by a space.

Output Format
Print the combinations with their replacements of string  on separate lines.

Sample Input
HACK 2

Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
from itertools import combinations_with_replacement

string,k=input().split()
string=sorted(string)

permutation_list=list(combinations_with_replacement(string,int(k)))
joined_list=["".join(element) for element in permutation_list]
print(*(i for i in joined_list),sep='\n')