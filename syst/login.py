login = False
password = ""
username = ""
while login != True:
    print("(l)ogin or (s)ign up?", end=' ')
    choice = input()
    if choice == "l":
        usernamei = input("Username: ")
        passwordi = input("Password: ")
        try:
            checkpass = open("users/" + usernamei + "/password.txt").read()
        except:
            print("User not found.")
            break
        if checkpass == passwordi:
            password = passwordi
            username = usernamei
            login = True
        else:
            print("Incorrect password.")
            break


cuser = open("tmp/cuser.txt", 'w')
cpass = open("tmp/cpass.txt", 'w')


cuser.write(username)
cpass.write(password)