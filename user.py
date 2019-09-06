class User:
    '''
    Tis class is going to hold and generate all the informations about the user
    '''
    user_list = []
    def __init__(self,username,password,email):
        '''
        this method helps to define the properties for our objects.
        '''
        self.username = username
        self.password = password
        self.email = email
    
    def save_user(self):
        '''
        this method saves user objects into the user_list
        '''
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        the method helps to delete a user from the user list
        '''
        User.user_list.remove(self) 
        
    @classmethod
    def find_by_email(cls,email):
        '''
        this method helps take the email and returns a username that matches it
        '''
        for user in cls.user_list:
            if user.email == email:
                return user 
            
    @classmethod
    def user_exist(cls,user):
        '''
        method that checks if a user exists from the user list
        '''
        for userc in cls.user_list:
            print(userc.username)
            if userc.username == user:
                
                return True
            
            return False                 
