
def f(x):
    return (x+3)*(x-10)

a=4.0
b=20.0

# Solution exists?
if f(a)*f(b)>0:
    print("Solution not found", f(a), f(b))
    exit(0)

sol=f((a+b)/2)
def abs(x):
    if x>0: return x
    return -1*x

while abs(f(sol)) > 0.0000000001:
    # print(f(sol), sol)
    if f(sol)*f(a) < 0:
        b=sol
    else:
        a=sol
    sol=(a+b)/2

print("final solution:",sol)
    

