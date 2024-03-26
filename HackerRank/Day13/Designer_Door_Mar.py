"""
Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

import math 
n,m=map(int,input().split())

for i in range(1,math.floor(n/2)+1):
    print((".|."*(i*2-1)).center(m,"-"))

print("WELCOME".center(m,"-"))

for i in range(math.floor(n/2),0,-1):
    print((".|."*(i*2-1)).center(m,"-"))