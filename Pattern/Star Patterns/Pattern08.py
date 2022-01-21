"""
Output:
number:5
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

#downward half-pyramid
#code:
n=int(input("number:"))
k=2*n-2
for i in range(n,-1,-1):
    for j in range(0,i+1):
        print("*", end=" ")
    print("\r")
