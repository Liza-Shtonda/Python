# побудувати матрицю випадкових дійсних чисел, дня неї знайти найбільше значення, медіану, середнє арифметичне

import random
import numpy as np

n=5
D=np.zeros((n,n), dtype=np.float)

for i in range(n):
    for j in range(n):
        D[i][j]=np.random.random()

print('max is: ', np.max(D))
print('median is: ', np.median(D))
print('average is: ', np.average(D))