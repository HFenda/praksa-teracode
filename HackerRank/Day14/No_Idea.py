"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if iEA, you add 1 to your happiness. If iEB, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format
The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format
Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1
"""
n,m=map(int,input().split())
array=[*map(int,input().split())]
set_A={*map(int,input().split())}
set_B={*map(int,input().split())}

happines=0

for number in array:
    if number in set_A:
        happines+=1
    if number in set_B:
        happines-=1

print(happines)