def f(x):
    return 1/(1+x)

a,b=0.0,1.0
n=10
step=(b-a)/n
y=[]
area = 0
for x in range(0,n+1):
    y=f(x*step+a)
    if x==0 or x == n:
        area += y
        print(1)
    elif x%2==0:
        area += 2*y
        print(2)
    else:
        area += 4*y
        print(3)

area *= 1/(n*3)
print(area)
print(y)
