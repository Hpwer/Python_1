<<<<<<< HEAD
=======

>>>>>>> 20d2beb66af6ec569374c69499e343d003d49fc4
a, b, c, d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

for i in range(c, d + 1):
    print("\t" + str(i), end="")

print()

for i in range(a, b + 1):
    print(i, end="")
    for n in range(c, d + 1):
        print("\t",i * n,sep="",end="")
    print()


