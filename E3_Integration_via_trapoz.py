def f(x):
    "This is the equation"
    return x**2

a,b=0.0,5.0 # Strating and end limit
n=10.0 # number of divisions
area = 0

step=(b-a)/n
cx=a

while cx!=b: 
    area += (f(cx)+f(cx+step))/2*step
    cx += step
print(area)
