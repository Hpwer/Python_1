from re import T


l1=input()
l2=input()
l3=input()
color=l2[1]
flag=True
if l1[1]!=color:
    flag=False
if l2[0]!=color:
    flag=False
if l2[1]!=color:
    flag=False
if l2[2]!=color:
    flag=False
if l3[1]!=color:
    flag=False
if flag==True:
    print("верно")
if flag==False:
    print("не верно")



    


