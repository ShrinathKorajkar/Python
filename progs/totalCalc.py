import os

os.chdir(os.path.dirname(__file__))
obj = open('bill.txt')
content = obj.readlines()
sum = 0
for num in content:
    sum += float(num)
print(sum)