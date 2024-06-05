import sys
input = sys.stdin.readline

bowl = str(input())


h = 0 
for i in range(1, len(bowl)):
    if bowl[i] == bowl[i-1]:
        h += 5
    if bowl[i] != bowl[i-1]:
        h += 10

print(h)