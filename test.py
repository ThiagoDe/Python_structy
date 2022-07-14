def get_initial(name):
    initial = name[0:1].upper()
    return initial
    

first_name = input('your name ')
f_init = get_initial(first_name)

last_name = input('your last name ')
last_init = get_initial(last_name)

print(f'Your initials {f_init} {last_init} ')
