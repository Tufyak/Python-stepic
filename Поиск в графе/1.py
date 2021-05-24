def fun(k):
    mark[k] = 1
    for i in range(n):
        if a[k][i] == 1 and mark[i]==0:
            fun(i)

a = [[1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]]
n = 8

for i in a:
  print(i)
print()
for i in range(n):
    r = 0
    for j in range(n):
        if a[i][j] == 1:
            print(j+1,end=' ')
            r += 1
    if r==0:
        print(0)
    else:
        print()