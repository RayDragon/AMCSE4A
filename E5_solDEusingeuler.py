def m(x,y):
    return 2+5*x+2*y
xs=[]
ys=[]
x0,y0=0,4

xs.append(x0)
ys.append(y0)
step=0.5
n=10
for s in range(0,n):
    xs.append(xs[s]+step)
    ys.append(ys[s]+m(xs[s],ys[s])*step)

print(xs)
print(ys)



