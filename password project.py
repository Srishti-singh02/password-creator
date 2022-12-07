'''import random
import string

def func():
    upper=0
    lower=0
    digiit=0
    spcl=0
    lowerd=string.ascii_lowercase
    upperd=string.ascii_uppercase
    digit=string.digits
    symbols=string.punctuation
    chars = lowerd+upperd+symbols+digit
#taking the length of password as input from the user
    password_len = int(input("'What is your password length:' "))
    if password_len<8:
        print("(Enter length greater than 7)")
        func()
#Generating the password
    else:
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password += password_char
        print(password)
#Checking the password stength
        for i in password:
            if i.isupper()==True:
                upper+=1
            if i.islower()==True:
                lower+=1
            if i.isdigit()==True:
                digiit+=1
            if ord(i) in range(33,48) or ord(i) in range(58,65):
                spcl+=1
        if upper!=0 and lower!=0 and digiit!=0 and spcl!=0:
            print("(GOOD PASSWORD)")
        else:
            print("(PASSWORD IS NOT GOOD)")
            print("(AGAIN CREATE A PASSWORD)")
            func()
func()
'''




