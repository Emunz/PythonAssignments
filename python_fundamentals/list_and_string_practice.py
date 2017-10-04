words = "It's thanksgiving day. It's my birthday too!"

string_2 = 'day'

#find and print words
print words.find(string_2)


#replace and print words
string_3 = 'month'

print words.replace(string_2, string_3)


#print the min of a list
x = [2,54,-2,7,12,98]

def lowest_num(list):
    print min(list)

lowest_num(x)

#print the max of a list
def highest_num(list):
    print max(list)

highest_num(x)

#print first and last values in a list
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print x[0], x[len(x)-1]

#sort list and print new list
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

x.sort()
print x
y = x[:len(x)/2]
z = x[len(x)/2:]

z.insert(0, y)

print z