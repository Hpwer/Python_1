n=int(input())
x=int(input())
p=int(input())
if p<n:
    print("низкий пульс")
if p>x:
    print("высокий пульс")
if p>=n and p<=x:
    print("пульс в норме")

       