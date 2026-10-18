#Write a program to check if user has entered correct userid and password.

userid= 'iblamesamm7'
password= 'Samarth@1234'

uid= input("Enter the userid from user:")
passw= input("Entr the password from user:")

if(uid == userid and passw == password):
    print("Logged in successfully.")

else:
    print("Wrong username or password.")
