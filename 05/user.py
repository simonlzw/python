userdb = {'alice' : 'alice' , }
def register():
    username = input('Username:')
    if username not in userdb:
        password = input('Password:')
        userdb[username] = password
    else:
        print('Please Enter Username or Username Exists')

def login():
    username = input('Username:')
    password = input('Password:')
    if (username , password) in userdb.items():
        print("Login Success")
    else:
        print("Login Fail")

def show_menu():
    prompt = """(0)Sign in
(1)Login
(2)Exit
Please Select (0/1/2): """

    while 1 :
        choice = input(prompt)
        if choice not in ['0' , '1' , '2']:
            print('Invalid Enter,Please Retry.')
            continue
        if choice == '0' :
            register()
        elif choice == '1' :
            login()
        else:
            print('Bye-bye')
            break

if __name__ == '__main__' :
    show_menu()