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