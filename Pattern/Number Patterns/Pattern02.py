"""
Output:
number:7
1  
1  1  
1  2  1  
1  3  3  1  
1  4  6  4  1  
1  5  10  10  5  1  
1  6  15  20  15  6  1  


"""

#Pascal's Triangle
#code:
n=int(input("number:"))
def pattern(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print(function(i,j) ," ", end="")
        print()

def function(n, k):
    res=1
    if(k> n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res
pattern(n)
