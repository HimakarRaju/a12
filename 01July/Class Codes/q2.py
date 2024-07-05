try:
    mylist = [1, 2, 3, 4]
    print(mylist[7])
except IndexError:
    print("This index does not exist")
    try:
        mylist = [1, 2, 3, 4]
        print(mylist[3])
    except IndexError:
        print("This index does not exist")
