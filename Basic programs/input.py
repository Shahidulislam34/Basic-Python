li = [{0, 0}]

n = int(input())

for i in range(1, n + 1) :
    pair = list(map(int, input().split()))
    li.append(pair)

for i in range(1, n + 1) :
    print(li[i][0], li[i][1])

ch = 50
print(ch)