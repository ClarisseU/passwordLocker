from user import User
from credentials import Credentials  
  
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
    
def delete_user(username):
    '''
    function to remove a username
    '''
    username.delete_user()  
    
def find_user(email):
    '''
    function that finds a user by email and returns the username
    '''
    return User.find_by_email(email)      