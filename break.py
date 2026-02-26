a=[1,3,4,5,7,8,9]
val = int(input("enter the value:"))
for i in a:
    if i == val:
        print(i)
        break
else:    
    print("not found")
        