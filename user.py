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