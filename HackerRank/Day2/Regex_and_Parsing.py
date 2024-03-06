"""
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge. For example, this code:
"""

import re
import email.utils

if __name__ == '__main__':
    
    pList=[]
    n=int(input())
    
    for _ in range(n):
        person= input().split()
        pList.append(person)
    
    for i in pList:
        regex = r'^[a-zA-Z][a-zA-Z0-9\._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$' #ovaj dio sam istrazio na internetu 
        if re.match(regex, i[1]):                                       
            print(i[0]+' '+i[1])
        