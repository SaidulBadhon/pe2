import json;
from getpass import getpass

import sys
from termcolor import colored, cprint

def colorPrint(text, colorName):
    return print(colored(text, colorName))

colorPrint('Hey, Welcome to The "Authentication System" app.', "green")
colorPrint("by Saidul Badhon", "green")
print("")
colorPrint("This app saves user data in local storage as plain text.", "grey")
cprint("Please do not save/signup with your real password here.", 'red', attrs=['bold'], file=sys.stderr)
print("")
print("")

users = []; 
with open('users.json', 'r') as f:
    users = json.load(f)

retry = True;
while retry == True:
    auth_type = input("How do you want to use this app? Login or Signup? ")
    
    print(auth_type.lower())

    if(auth_type.lower() == "login" or auth_type.lower() == "l"):
        
        print("")
        colorPrint("Let's log you into our system:", "green")
        colorPrint("------------------------------", "green")

        email = input("Email: ")
        password = getpass("Password: ")
        
        userObj = {};
        for user in users:
            if(user["email"] == email and user["password"] == password) :
                userObj = user;

        if(len(userObj) > 0):
            print("")
            print("Welcome back,", userObj["user_name"],"!")
            print("Here is your data: ", userObj)
            print("")
        else:
            print("")
            cprint("Invalid email or passowrd, try again later", 'red', attrs=['bold'], file=sys.stderr)
            print("")

    elif(auth_type.lower() == "signup") or auth_type.lower() == "s":
        print("")
        colorPrint("Let's sign you into our system:", "green")
        colorPrint("-------------------------------", "green")

        user_name = input("User Name: ")
        email = input("New Email: ")

        has_user = False;

        for user in users:
            if(user["email"] == email) :
                print("")
                cprint("Email already exist. Please login.", 'red', attrs=['bold'], file=sys.stderr)
                print("")
                has_user = True
                break

        if(has_user == False):
            password = getpass("New Password: ")

            data_to_save = {"user_name": user_name, 'email': email, 'password':password}
            users.append(data_to_save)

            with open('users.json', 'w') as f:
                json.dump(users, f, indent=2)
            
            colorPrint("Signup successful.", "green")
            print("")

    else:
        print('Fail request. Please type "login" or "signup"\n')
