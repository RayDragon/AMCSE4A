import numpy as np

a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[1],[2],[4]]
a=np.matrix(a)
b=np.matrix(b)

print("a\n",a)
print("b\n",b)
print("a+b:\n", a+b)
print("a*b:\n", a*b)
print("a-b:\n", a-b)
