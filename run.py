from user import User
from credentials import Credentials  
  
def create_user(username,password,email):
    '''
    funcion to create a new contact
    '''
    new_user = User(username,password,email) 
    return new_user 

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