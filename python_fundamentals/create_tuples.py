my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

new_list = []
def dictionary_to_tuples(dictionary):
    for name, phone in my_dict.iteritems():
        user_tuple = name, phone
        new_list.append(user_tuple)
    return new_list       



print dictionary_to_tuples(my_dict)
