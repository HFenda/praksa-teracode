"""
Input Format
First line contains n, the number of rational numbers.
The i-th of next n lines contain two integers each, the numerator( Ni ) and denominator( Di ) of the i-th rational number in the list.

Output Format
Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than .

Sample Input 0
3
1 2
3 4
10 6

Sample Output 0p
5 8
"""
from fractions import Fraction
from functools import reduce

def product(fracs):
    t=reduce(lambda x,y: x*y,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)