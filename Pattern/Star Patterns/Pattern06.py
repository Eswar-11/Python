"""
Output:
number:5
* 
* * 
* * * 
* * * * 
* * * * *
"""

#code:
n=int(input("number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
