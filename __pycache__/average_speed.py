a=int(input("enter speed of a: "))
b=int(input("enter speed of b: "))
c=int(input("enter speed of c: "))

ave=(a+b+c)/3
print("average is ",ave)

if ave>a and ave>b and ave>c:
    print("%d is higher than %d,%d,%d"%(ave,a,b,c))
else:
    print("%d is lesser than %d,%d,%d"%(ave,a,b,c))