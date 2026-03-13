pattern = input("Enter pattern(normal/reverse/tree/l): ")
n = int(input("Enter number: "))

if pattern == "normal":
    for i in range(1,n+1):
        print("*"*i)

elif pattern == "reverse":
    for i in range(n,0,-1):
        print("*"*i)

elif pattern == "tree":
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*(2*i-1))

elif pattern == "l":
    for i in range(n):
        if i == n-1:
            print("*"*n)
        else:
            print("*")

else:
    print("Wrong type")