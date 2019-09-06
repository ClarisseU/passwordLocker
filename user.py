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
