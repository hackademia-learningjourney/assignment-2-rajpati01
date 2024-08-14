'''
Assignment 2 - Deadline (Saturday, August 17, 8:00 PM)

#QUESTION WAP that first gives 2 options:

Sign up
Sign in
when 1 is pressed user needs to provide following information

Username, 2. Password, 3. Mobile number All this information is saved in a file everytime a new user signs up the same file is updated (hint Append over the same file)
when 2 is pressed User needs to provide username and password this username and password is checked with username and password in the database if matched: welcome to the device and show their phone number else: terminate the program saying incorrect credentials

Do it using json files, save everything to json and load from json

'''

import json

def save_to_json(data, filename = 'login_info.json'):
    # save the given data to a JSON file.
    with open(filename, 'w') as f:
        json.dump(data, f , indent=4)

def load_form_json(filename = 'login_info.json'):
    # Load data from a JSOn file.
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file does not exit, return an empty dictionary
        return {}

def Signup_Signin():
    # Load existing data from JSON file
    users_data = load_form_json()
    
    choice = int(input('Press 1 to Sign up or 2 to Sign in: '))
    
    if choice == 1:
        username = input('Enter username: ')
        if username in users_data:
            print('Username already exists. Please choose a different username.')
            return

        password = input('Enter password: ')
        phone_number = input('Enter phone number: ')
        
        # add new user to the dictionary
        users_data[username] = {
            "password": password,
            "phone_number": phone_number
        }
        
        # save the updated dictionary to the JSON file
        save_to_json(users_data)
        print('Sign up successcul!')
        
    elif choice == 2:
        username = input('Enter username: ')
        password = input('Enter password: ')
        
        # check if the user exists and rhe password matches
        if username in users_data and users_data[username]['password'] == password:
            print(f'Welcome to the device! Your phone number is {users_data[username]["phone_number"]}')
        else:
            print('Invalid username or password')
            
    else:
        print('Invalid choice')
            

Signup_Signin()
