n=input("enter the string: ")
k=len(n)
for i in range(1,k+1):
    for j in range(1,k+1):
        if(i==j or i+j==k+1):
            print(n[j-i],end=" ")
        else:
            print(" ",end=" ")
    print()
  