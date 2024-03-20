"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

alison heck=>Alison Heck
Given a full name, your task is to capitalize the name appropriately.
"""

def solve(s):
    s_list = list(s)
    if s_list:
        s_list[0] = s_list[0].upper()
    for i in range(1, len(s_list)):
        if s_list[i-1] == " " and s_list[i].isalpha():
            s_list[i] = s_list[i].upper()
    return ''.join(s_list)


if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result + '\n')