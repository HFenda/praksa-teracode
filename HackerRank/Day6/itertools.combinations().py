"""
Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format
A single line containing the string S and integer value k separated by a space.

Output Format
Print the different combinations of string S on separate lines.

Sample Input
HACK 2

Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

from itertools import combinations
string,k=input().split()
string=sorted(string)

for i in range(1,int(k)+1):
    combination_list=list(combinations(string,int(i)))
    joined_combination_list=[''.join(element) for element in combination_list]
    print(*(combination for combination in joined_combination_list),sep='\n')