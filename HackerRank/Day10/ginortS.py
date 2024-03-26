"""
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format
A single line of input contains the string S.

Output Format
Output the sorted string .

Sample Input
Sorting1234

Sample Output
ginortS1324
"""
word=input()
lowercase=[]
uppercase=[]
digits=[]

for char in word:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    elif char.isnumeric():
        digits.append(char)
    
digits=sorted(digits)

print("".join(sorted(lowercase)+sorted(uppercase)+sorted(digits,key=lambda x: int(x) % 2 == 0)))