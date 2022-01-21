"""
Output:
number:5
A
B B
C C C
D D D D
E E E E E


"""

#right alphabetical triangle
#code:
n=int(input("number:"))
def pattern(n):
    x=65
    for i in range(0,n):
        ch = chr(x)
        x=x+1
        for j in range(0, i+1):
            print(ch, end=" ")
        print()
pattern(n)
