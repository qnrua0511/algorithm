#BOJ 11052
import sys
input=sys.stdin.readline
n=int(input())
g=[]
for _ in range(n):
    g.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] and g[k][j]:
                g[i][j]=1

for i in range(n):
    print(*g[i])