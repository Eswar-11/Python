"""
Output:
number:5
        A 
       B B 
      C C C 
     D D D D 
    E E E E E 
   A A A A A A 
    B B B B B 
     C C C C 
      D D D 
       E E 
        F


"""

#code:
n=int(input("number:"))
def pattern(n):
    k = 2 * n - 2
    x=65
    for i in range(0, n):
        ch=chr(x)
        x=x+1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
    k = n - 2
    x=65
    for i in range(n, -1, -1):
        ch=chr(x)
        x=x+1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
pattern(n)
