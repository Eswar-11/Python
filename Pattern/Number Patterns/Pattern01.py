"""
Output:
number:5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""

#code:
n=int(input("number:"))
x=0
for i in range(0,n):
    x += 1
    for j in range(0, i+1):
        print(x, end=" ")
    print()
