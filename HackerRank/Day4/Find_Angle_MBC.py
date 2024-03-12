"""
ABC is a right triangle, 90 at B.
Therefore, <ABC=90.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find <MBC (angle theta, as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format
Output <MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

Sample Input
10
10

Sample Output
45°
"""
import math

a=int(input())
b=int(input())

c=((a**2)+(b**2))**(1/2)
S=(a*b)/2
h=(S*2)/c

angle_radians=math.atan(a/b)
angle_degrees=round(math.degrees(angle_radians))

print(str(angle_degrees)+'\u00B0')