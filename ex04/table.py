from socket import inet_ntoa


a, b, c, d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

for i in range(c, d + 1):
    print("\t" + str(i), end="")

print()

for i in range(a, b + 1):
    print(i, end="\t")
    for n in range(c, d + 1):
        print(i * n, end="\t")
    print()


