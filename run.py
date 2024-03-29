#!/usr/bin/env python3
#!/usr/bin/env python2
from user import User
from credentials import Credentials  
import random
import string

def randomString(stringLength=10):
    words = string.ascii_letters
    return ''.join(random.choice(words) for i in range(stringLength))

def create_account(username,password,email):
    '''
    function to create an account
    '''
    new_user = User(username, password, email)
    return new_user
  
def create_user(username,password,email):
    '''
    funcion to create a new contact
    '''
    new_user = User(username,password,email) 
    return new_user 


def create_cred(socialMed,username,password,email):
    '''
    function to create a new credential
    '''
    new_cred = Credentials(socialMed,username,password,email)
    return new_cred

def save_user(username):
    '''
    function to save a user
    '''
    username.save_user()
    
def save_cred(username):
    '''
    function to save a created credential
    '''
    username.save_cred()
    
def delete_user(username):
    '''
    function to remove a username
    '''
    username.delete_user()  
    
def delete_cred(username):
    '''
    function to delete a credential
    '''
    username.delete_cred()    
    
def find_user(email):
    '''
    function that finds a user by email and returns the username
    '''
    return User.find_by_email(email)

def find_cred(username):
    '''
    function to find a credential
    '''
    return Credentials.find_by_username(username)

def check_existing_user(username):
    '''
    function to check if the user exists
    '''
    return User.user_exist(username)

def check_existing_cred(username):
    '''
    function to chexk the existing credentials
    '''
    return Credentials.cred_exist(username)

def display_users():
    '''
    function that displays all the saved users
    '''
    return User.display_user()

def display_creds():
    '''
    function that returns all the saved credentials
    '''
    return Credentials.display_creds()

def main():
    print("Welcome to Password Locker. what is your name?")
    user_name = input()
    
    print(f'Hello {user_name}. what would you like to do?')
    print('\n')
    
    while True:
        print('use these short codes : login - to login if you have an account, cu - create a username, du - display usernames, fu - find a username, ex - exit the username list')
        print('\n')
        print('or input the following codes for the credentials: cc - create credentials, dc - displays the credentials, fc - find the credential, ex - to exit')
        short_code = input().lower()
        
        if short_code == 'cu':
            print('New user')
            print('-'*10)
            
            print('user name....')
            username = input()
            
            print('password ....')
            password = input()
            
            print('email ....')
            email = input()
            
            save_user(create_user(username,password,email))
            print('\n')
            print(f'new user {username} created')
            print('\n')
            
        elif short_code == 'du' :
            if display_users():
                print('Here is a list of all users')
                print('\n')
                
                for user in display_users():
                    print(f'{user.username} ... {user.email}')
                    print('\n')
                    
            else :
                print('\n')
                print('there is no saved users')
                print('\n')
            
        elif short_code == 'fu':
            print('enter the email you want to search for')
            
            search_email = input()
            if check_existing_user(search_email):
                search_user = find_user(search_email)
                print(f'{search_user.username} {search_user.email}')
                print('-'*20)
                print(f'email ....{search_user.email}')
                
        elif short_code == 'login':
            print('LOG IN')
            print('-'*10) 
            print('\n') 
            print('enter the username you have created:')
            username = input()
            if check_existing_cred(username):
                searched_username = find_cred(username)   
                print(f'{searched_username.username}  {searched_username.email}')
                print('-'*20)
                print('\n')
                print('successfully logged in')   

        else:
            print(f'Hey {username}. would you want to continue and register or check the credentials?')
            print('\n')
    
            while True:
                print('use these codes : cc - create a credential, dc - display credentials, fc - find a credential, del - delete a credential, ex - exit the credential list')
                print('\n')
                code = input().lower()
        
                if code == 'cc':
                    print('Add a credential')
                    print('-'*10)
            
                    print('enter the social media...')
                    socialMed = input()
            
                    print('user name....')
                    username = input()
                    
                    print('Do you want to create your own password or it to be generated automatically')
                    print("\n")
                    print('gn for generating the password automatically or cp to create a password')
                    shrtcd = input()
                    if shrtcd == 'gn':
                        print ("your new password is: ", randomString(10) )
                    else:
                            
                        print('password ....')
                        password = input()
            
                    print('email ....')
                    email = input()
            
                    save_cred(create_cred(socialMed,username,password,email))
                    print('\n')
                    print(f'new credential {username} created')
                    print('\n')
            
                elif code == 'dc' :
                    if display_creds():
                        print('Here is a list of all credentials')
                        print('\n')
                
                        for cred in display_creds():
                            print(f'{cred.socialMed} ... {cred.username} ... {cred.password}')
                            print('\n')
                    
                    else :
                        print('\n')
                        print('there is no saved credentials')
                        print('\n')
            
            
                elif code == 'fc':
                    print('enter the username you want to search for')
            
                    search_username = input()
                    if check_existing_cred(search_username):
                        search_cred = find_cred(search_username)
                        print(f'{search_cred.socialMed} {search_cred.username} {search_cred.email}')
                        print('-'*20)
                        print(f'email ....{search_cred.email}')
                        
                elif code == 'del':
                    print('Deleting a credential')
                    print('-'*10)
                    print('\n')
                    print('enter the username you want to delete')
                    search_username = input()
                    
                    print(check_existing_cred(search_username))
                    
                    if check_existing_cred(search_username):
                        searched_username = find_cred(search_username)
                        print(f'{searched_username.username}  {searched_username.email}')
                        print(''*10)
                        searched_username.delete_cred()
                        print('credential deleted')
                                 
                
                
                elif code == 'ex':
                    print('Bye....')
                    break
                else:
                    print('i did not get that. please use the codes below')         
                                        
            
if __name__ == '__main__':

    main()            
      