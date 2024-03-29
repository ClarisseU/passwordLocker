class Credentials:
    '''
    This class is going to hold information about the credentials
    '''
    cred_list = []
    def __init__(self,socialMed,username,password,email):
        '''
        will hold the properties for our objects
        '''    
        self.socialMed = socialMed
        self.username = username
        self.password = password
        self.email = email
        
    def save_cred(self):
        '''
        this method saves the credential
        '''
        
        Credentials.cred_list.append(self) 
        
    def delete_cred(self):
        '''
        the method helps to delete a user from the user list
        '''
        Credentials.cred_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        '''
        helps find a username
        '''
        for cred in cls.cred_list:
            if cred.username == username:
                return cred 
            
    @classmethod
    def cred_exist(cls,username):
        '''
        method that checks if a user exists from the user list
        '''
        for crede in cls.cred_list:
            print(crede.username)
            if crede.username == username:
                
                return True
            
            return False   
        
    @classmethod
    def display_creds(cls):
        '''
        method that returns the user list
        '''
        return cls.cred_list                     