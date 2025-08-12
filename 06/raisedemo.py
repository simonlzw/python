def pass_check():
    password = input("Password: ")
    if len(password) >= 8 :
        return password
    ex = Exception("The password length is insufficient")
    raise ex

if __name__ == '__main__' :
    user_pwd = pass_check()
    print(user_pwd)

