"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)

"""
from itertools import groupby
string=input()
charList=[]
resultList=[]

for char in string:
    charList.append(char)
    
for key,group in groupby(charList,key=lambda x: x):
    resultList.append(f"({len(list(group))}, {key})")

print(' '.join(resultList))