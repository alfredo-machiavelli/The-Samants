import sys
import json

from bson import ObjectId
from getpass import getpass
from bson.json_util import dumps
from pymongo import MongoClient
import pymongo


client = MongoClient("mongodb+srv://suprita:jungK00K@supritadb.m2chzrd.mongodb.net/?retryWrites=true&w=majority")
db = client.UserDB
users = db.UserCollection0

# sample fieldst = {"Username": "suprita",
#         "First Name": "Suprita",
#         "Last Name": "Ashok",
#         "UserID": ObjectId(),
#         "Password": "password",
#         }


def encrypt(original_string, N, D):
    result = ""

    #we are going to loop through each char in the string
    #for every character in inputText
    #[::-1] means start at the end of the string + move back by 1 [hence the -1]

    for character in original_string[::-1]:

        # since space and ! are not encrypted
        if character == ' ' or character == '!':
            result = character + result


        else:

            #ord will return the ascii value of the char
            val = ord(character) + (N * D)

            # if the value is lower than 34, then we subtract the diff from 126
            if val < 34:
                val = 126 - (34 - val)

            #so if the value is higher than 126, then we add the diff to 34
            if val> 126:
                val = 34 + (val- 126)

            #chr is the letter associated with the ascii value
            #add this to the result
            result = chr(val) + result


    return result

def decrypt(encrypted_string, N, D):
    result = ""

    # we are going to loop through each char in the string
    # for every character in inputText
    # [::-1] means start at the end of the string + move back by 1 [hence the -1]
    for character in encrypted_string[::-1]:
        # characters space and ! are not encrypted
        if character == ' ' or character == '!':
            result = character + result
        else:
            val = ord(character) - N * D
            if val> 126:
                val = 34 + (val - 126)
            if val < 34:
                val = 126 - (34 - val)
            result = chr(val) + result

    return result

def login(name,pword,Error,ErrorMsg):
    username = name
    while users.find_one({"Username": username}) is None:
        Error = True
        ErrorMsg  = "Username not found. Please try again: "
        return
    thisUser =  users.find_one({"Username": username})
    correctPass = decrypt(str(thisUser["Password"]), 4, -1)
    password = pword
    while password !=  correctPass:
        Error = True
        ErrorMsg = "Incorrect password. Please try again: "
        return
    print("Login successful! Welcome " + thisUser["First Name"] + "!")
    return

def signup(username,password,Error,ErrorMsg): 
    firstName = "John"
   # while not firstName.isalnum():
       # firstName= input("Make sure your first name doesn't have any numbers!\n What's your first name? ")

    lasttName = "Doe"
   # while not lasttName.isalnum():
       # lasttName = input("Make sure your last name doesn't have any numbers!\n What's your lastname? ")

    
    while not username.isalnum() and  password.isalnum() :
        Error = True
        ErrorMsg =  "Make sure your username and/or password only contains numbers and letters!\n"
        return
                        


    newUser = {"Username": username,
            "First Name": firstName,
            "Last Name": lasttName,
            "Password": encrypt(password, 4, -1),
            }

    resource_id = users.insert_one(newUser).inserted_id
    print("Signup successful! Welcome " + firstName + "!")
    return

#def main():
    #print("Welcome to h/w library!")
   # try:
        #which =input("Would you login, signup, or exit the application?")
        #if which == "login":
            #login()
        #elif which == "signup":
           # signup()
       # elif which == "exit":
           # sys.exit()
    #except KeyboardInterrupt: print("\nGood Bye!")


#if __name__ == "__main__":
    ##main()
