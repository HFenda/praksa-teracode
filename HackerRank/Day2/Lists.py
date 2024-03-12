"""
Consider a list (list = []). You can perform the following commands:

1.insert i e: Insert integer  at position .
2.print: Print the list.
3.remove e: Delete the first occurrence of integer .
4.append e: Insert integer  at the end of the list.
5.sort: Sort the list.
6.pop: Pop the last element from the list.
7.reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    list=[]
    
    for i in range(N):
        command=input()
        
        typ, *data=command.split()
        
        if typ=="insert":
            index=int(data[0])
            value=int(data[1])
            list.insert(index,value)
            
        if typ=="print":
            print(list)

        if typ=="remove":
            index=int(data[0])
            list.remove(index)
            
        if typ=="append":
            value=int(data[0])
            list.append(value)
            
        if typ=="sort":
            list.sort()
            
        if typ=="pop":
            list.pop()
            
        if typ=="reverse":
            list.reverse()
            
