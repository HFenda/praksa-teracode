"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    
    resoults=[]
    grades=[]
    secLowest=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        resoults.append([name,score])
    
    grades.sort()            #sortiranje ocjena
    grades=list(set(grades)) #eliminacija duplikata
    secScore=grades[1]       #spremanje drugoplasirane ocjene
    
    for i in (resoults):
        if(i[1]==secScore):
            secLowest.append(i[0])
    
    secLowest.sort()         #abecedno sortiranje
    
    for i in secLowest:
        print(i)