# password = "GREEHouse"
password = input('Please enter your password: ')
if password == 'GREEHouse':
    print('Welcome to colours game')
    colour = input('Enter your favourite colour: ')
    age = int(input('Enter your age: '))
    if colour == 'white' and age > 10:
        print('You love peace.')
    elif colour == 'green' and age > 15:
        print('You love nature')
    elif colour == 'red' and age > 15:
        print('You love rose.')
    elif colour == 'pink' and age > 15:
        print('You are a girl.')
    elif colour == 'pink' and 5 < age < 15:
        print('You have a weird choice.')
    elif colour == 'blue' and age > 10:
        print('You love the Sea.')
    elif colour == 'indigo' and age > 15:
        print('You have a decent choice.')
    elif colour == 'violet' and age > 20:
        print('you have a good choice.')
    elif colour == 'yellow' and age > 15:
        print('You love the Sun.')
    elif colour == 'purple' and age > 20:
        print('You have a decent choice.')
    else:
        print('You are a boring person.')
else:
    print("Wrong! password entered.")
