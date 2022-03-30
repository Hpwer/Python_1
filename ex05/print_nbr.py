n,m=input().split()
n=int(n)
m=int(m)
i = n * m
e = 1_000_000_000
while( abs(i)// e == 0 and e > 1):
    e = e//10
if i < 0:
    print("-")
    i = abs(i)
while(e > 0):
    print(i//e%10)
    e=e//10

    