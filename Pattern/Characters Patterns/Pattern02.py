"""
Output:
number:5
    A
   B C
  D E F
 G H I J
K L M N O


"""

#code:
n=int(input("number:"))
def pattern(n):
    k=n-1
    x=65
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            ch=chr(x)
            print(ch, end=" ")
            x +=1
        print()
pattern(n)
