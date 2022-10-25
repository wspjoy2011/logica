login = 'admin'
password = '123456'
first_name = 'Jack'
tries = 0

while tries < 3:
    user_login = input('Enter your login: ')
    user_password = input('Enter your password: ')

    if user_login == login and user_password == password:
        print(f'Welcome, {first_name}!')
        break
    else:
        tries += 1
        print('Bad authentication!')
