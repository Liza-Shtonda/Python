# побудувати квадратну матрицю, у якої a[i][j]=C(i,j)+C(j,i)

import numpy as np
n=5
D=np.zeros((n,n), dtype=np.int32)
D[0]=1
D.T[0]=1

for i in range(1, n):
    for j in range(1,i+1):
        D[i, j] = -D[i, j-1] * (i - j + 1) // j

for i in range(1, n-1):
    for j in range(i+1,n):
        D[i, j] = -D[i-1, j] * (j - i + 1) // i

print(D)