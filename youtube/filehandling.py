# fi = open('data.txt', 'r')
with open('python/youtube/data.txt', 'rt') as fi:
    for line in fi:
        print(line, end='')
    fi.seek(0)
    print()
    print(fi.read())
    print()
    fi.seek(0)
    print(fi.read(10))
    print()
    fi.seek(0)
    print(fi.tell())
    print(fi.readline())
# fi.close()
with open('python/youtube/data.txt', 'a') as fi:
    lines = ['this ', 'is ', 'lines \t']
    fi.write('this is appended\t')
    fi.writelines(lines)
