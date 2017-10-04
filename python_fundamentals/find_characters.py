
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna', 'lol']

char = 'n'
new_list = []

def find_character(list):
    for x in list:
        for letter in x:
            if (letter == char):
                new_list.append(x)
                break

        

    print new_list
find_character(word_list)