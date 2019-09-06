#!/usr/bin/env python3
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
    
def save_cred(username):
    '''
    function to save a created credential
    '''
    username.save_cred    
    
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
    return User.display_users()

def display_creds():
    '''
    function that returns all the saved credentials
    '''
    return Credentials.display_creds()


      