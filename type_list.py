
list_1 = ['magical unicorns',19,'hello',98.98,'world']

list_2 = [2,3,1,7,4,12]

list_3 = ['magical','unicorns']

list_4 = [0, 'Evan', 88, 'sucks', 3, 'so', 5, 23, 4, 2, 'much', 9, 'lol', 'no', 'I', 6, 'don\'t', 10, 'computer', 'shut', 'up', 20,]






def listType(list):
    int_count = 0
    str_count = 0
    sum = 0
    built_string = "String:"

    for x in list:
        if(type(x) == int or type(x) == float):
            int_count += 1
            sum += x
        if(type(x) == str):
            str_count += 1
            built_string = built_string + ' ' + x



    if(int_count == 0):
        print "The list you entered is of string type"
    elif(str_count == 0):
        print "The list you entered is of integer type"
    else:
        print "The list you entered is of mixed type"
    
    if(str_count != 0):
        print built_string
    if(int_count != 0):
        print "Sum:", sum

    



listType(list_4)