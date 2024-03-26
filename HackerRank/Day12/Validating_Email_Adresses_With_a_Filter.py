"""
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores .
The website name can only have letters and digits .
The extension can only contain letters .
The maximum length of the extension is .

Input Format
The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""
import re
import email.utils

def fun(s):
    regex=r'^[a-zA-Z][a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.match(regex,s):
        return True
    else:
        return False
        
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)