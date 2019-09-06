from user import User
from credentials import Credentials  
  
def create_user(username,password,email):
    '''
    method to create a new contact
    '''
    new_user = User(username,password,email) 
    return new_user    