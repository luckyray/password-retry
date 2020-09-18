password = 'a123456'
chance = 3
while chance > 0:
    user_input = input('Please enter the password: ')
    print('password verificaiton........')
    if user_input == password:
        print('You have entered the correct password.')
        print('Your access is granted.')
        break
    else:
        chance = chance - 1
        print('Password verification failed.')
        print('Your access is denie')
        print('You have ', chance, ' chance/s left')
