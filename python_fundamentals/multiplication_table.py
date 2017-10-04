def multiply_rows():
    row = ' '
    for x in range(13):
        row = row + ' ' + str(x)
    print row
    row = ' '
    for a in range(13):
        if(a != 0):
            row = row + ' ' + str(a)
        if(a != 0):
            for b in range(13):
                if(b != 0):
                    row = row + ' ' + str(b*a)

            print row
            row = ' '


multiply_rows()
        
