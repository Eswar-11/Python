"""
Output:
number:5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

"""

n=int(input("number:"))
for i in range(0,n):
    for j in range(0,i +1):
        print("*", end=" ")
    print("\r")
for i in range(n,-1,-1):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
