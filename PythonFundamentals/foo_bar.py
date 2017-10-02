def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


for x in range(1, 40):
    if(x < 10):
        if(x == 1):
            print str(x) + 'FooBar'
        elif(x == 6):
            print str(x) + 'FooBar'
        elif(is_square(x) == True):
            print str(x) + 'Bar'
        elif(x % 5 == 0 or x % 7 == 0 or x % 3 == 0):
            print str(x) + 'Foo'
        else:
            print str(x) + 'FooBar'
    else:
        if(x % 3 != 0 and x % 2 != 0 and x % 5 != 0 and x % 6 != 0 and x % 7 != 0 and x % 8 != 0 and x % 9 != 0):
            print str(x) + 'Foo'
        elif(is_square(x) == True):
            print str(x) + 'Bar'
        else:
            print str(x) + 'FooBar'

