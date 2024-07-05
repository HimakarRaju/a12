# Nested ifs

x = 15
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is greater than 20")
        if 10 > x > 20:
            print("x is greater than 10 and less than 20")
            if x < 10:
                print("x is less than 10")
