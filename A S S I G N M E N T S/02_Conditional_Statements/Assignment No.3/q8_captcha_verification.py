# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha).

import random

uid= "iblamesamm7"
passw= "Samarth@123"

userid= input("Enter username: ")
pass_word= input("Enter password: ")

if(userid==uid and pass_word==passw):
    print("Logged in successfully.")
    
    # captcha= 4567
    # user_input= int(input("Enter numbers shown in above."))
    # if(user_input==captcha):/

    captcha= random.randint(1000,9999)
    print("Captcha: ", captcha)

    user_input= int(input("Enter the Captcha: "))
    if(user_input == captcha):
        print("Acces granted")
    else:
        print("Access denied")

else:
    print("Wrong username and password.")

