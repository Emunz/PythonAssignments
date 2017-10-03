def odd_even(x,y):
    for x in range(x,y):
        if(x % 2 != 0):
            print "Number is " + str(x) + ". This is an odd number."
        else:
            print "Number is " + str(x) + ". This is an even number."

odd_even(1, 2001)

def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr

a = [2, 4, 10, 16]
b = multiply(a, 5)

print b

new_arr = []
def layered_multiply(arr):
    for x in arr:
        inception_arr = []
        for i in range(0,x):
            inception_arr.append(1)
        new_arr.append(inception_arr)
    return new_arr


y = [2,4,5]
x = layered_multiply(multiply(y,3))

print x
