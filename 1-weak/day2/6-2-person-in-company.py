n = int(input())
l_set = set()

for _ in range(n):
    name, log = map(str, input().split())

    if log == 'enter':
        l_set.add(name)
    else:
        l_set.remove(name)

list = list(l_set)
list.sort(reverse=True)

for i in list:
    print(i)