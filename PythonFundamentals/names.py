users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def roll_call ():
    for people, names in users.iteritems():
        print people
        number = 0
        for data in names:
            name = ''
            number += 1
            for key, value in data.iteritems():
                name += value + ' '
            print str(number) + ' - ' + name + '- ' + str(len(name)-name.count(' '))
            name = ''
roll_call()