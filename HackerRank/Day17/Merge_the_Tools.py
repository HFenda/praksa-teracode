"""
Consider the following:

A string,s, of length n where s=c0c1...cn-1.
An integer,k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index x<j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.

Function Description
Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze

Prints
Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format

The first line contains a single string, s.
The second line contains an integer,k, the length of each substring.

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output

AB
CA
AD
"""
from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)