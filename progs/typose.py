# PROGRAM TO FIND TYPOSE
with open('D:/visual studio/Python/progs/typosedata.txt', 'r') as file:
    content = file.read()
    print('file contents are : \n\n' + content)
    file.seek(0)
    lineno = 0
    for line in file.readlines():
        lineno += 1
        mylist = line.split(' ')
        for i in range(len(mylist) - 1):
            if mylist[i] == mylist[i + 1]:
                print('\ntypose error found at line no : ' + str(lineno) +
                      ' at position : ' + str(i + 1))
                print('typose : ' + mylist[i] + ' ' + mylist[i + 1])

    print('\nthank you :)')
