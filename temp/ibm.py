def changeCase(inputStr, choice):
    mylist = inputStr.split()
    if choice == 1:
        # camelcase
        for i in range(1, len(mylist)):
            mylist[i] = mylist[i][0].upper() + mylist[i][1:]
        return "".join(mylist)

    elif choice == 2:
        # kebabcase
        return "-".join(mylist)

    elif choice == 3:
        # snakecase
        return "_".join(mylist)

    elif choice == 4:
        # pascalcase
        for i in range(len(mylist)):
            mylist[i] = mylist[i][0].upper() + mylist[i][1:]
        return "".join(mylist)


print(changeCase("hello world", 1))
print(changeCase("hello world", 2))
print(changeCase("hello world", 3))
print(changeCase("hello world", 4))