import numpy as np 
A=np.mat([[3,2],[1,0]])
print("A:\n",A)
print("Eigen values:\n", np.linalg.eigvals(A))