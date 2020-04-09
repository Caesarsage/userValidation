import random as rd
import string

def user_details():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("email: ")
    return [first_name,   last_name,email]


def generate_password(first_name,last_name):
    random_string = string.ascii_letters
    random = "" .join(rd.	choice(random_string)for i in range(5))
    password = str(first_name[ :2] + last_name[-2:] + random)
    return password



def generate_new_password(new):
    accepted = str(input("Do you like the password?: YES or NO  \n "))
    if accepted.lower() == "no":
        new_password = input("Enter New Password: ")
        while len(new_password) < 7:
        	print("Character must equal or greater than 7 in length \n")
        	new_password = input("Enter New Password: ")
        else:
        	new = new_password
        	return str(new)
    elif accepted.lower() == "yes" :
     return str(new)
    else:
     return generate_new_password (new)

def mains():
    user = user_details()
    user_password = generate_password(user[0], user[1])
    print(f"Generated Password:{user_password}")
   
    new_password = generate_new_password(user_password)
    print ('your new password is: ' +str(new_password))
    user.append(str(user_password))
    return user		

def decision(ask):
    ask.append(mains())
    another_user = input("Do you want to input another user? yes or no : \n").lower()
    if another_user == "yes":
        return decision(ask)
    elif another_user == "no":
    	return (ask)
    
data=[]

data.append(decision(data))
data.pop(-1)
labels=["First Name:","Last Name:","Email:","Password:"]

print('*** FULL DETAILS OF THE USER(S)***')
for i in range(0, len(data)):
    print('******User {0}'.format(i+1) + ' Details******')
    for x in range(0,len(data[i])):
        print(labels[x]+' '+data[i][x])