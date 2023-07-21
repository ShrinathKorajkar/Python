n = int(input())
entry = list(map(int, input().split()))
exit = list(map(int, input().split()))
dic = {}
for i in range(len(entry)):
    dic[entry[i]] = exit[i]

entry.sort()
maxCount = 0
time = 0
count = 0
for i in entry:
    count += 1
    for j in exit:
        if j <= i and i in dic.keys():
            del dic[i]
            count -= 1
    if maxCount < count:
        maxCount = count
        time = i

print(time, maxCount)

# n = 5
# entry = [1, 2, 10, 5, 5]
# exit = [4, 5, 12, 9, 12]