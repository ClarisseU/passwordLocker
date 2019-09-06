import unittest
from credentials import Credentials

class TestCred(unittest.TestCase):
    '''
    Class that tests the case for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credentials('Instagram','Klarys','python3','clarisseum@gmai.com')
        
    def test_init(self):
        '''
        first_test is to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.socialMed,'Instagram')
        self.assertEqual(self.new_cred.username,'Klarys')
        self.assertEqual(self.new_cred.password,'python3')
        self.assertEqual(self.new_cred.email,'clarisseum@gmai.com')
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.cred_list = []
        
    def test_save_cred(self):
        '''
        this is a test to check if the account is saved
        '''
        
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)
        
    def test_multi_user(self):
        '''
        the method is to test if we can save multiple credential objects to our credential list
        '''
        self.new_cred.save_cred()
        test_cred = Credentials ('Instagram','Klarys','python3','clarisseum@gmai.com')
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2) 
        
    def test_delete_cred(self):
        '''
        the method tests if we can remove a credential from our credential list
        '''
        self.new_cred.save_cred()
        test_cred = Credentials ('Test','user','password','user@gmail.com')
        test_cred.save_cred()
        
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list),1)
        
    def test_find_by_username(self):
        '''
        test to check if we can find a user byt username and display information
        '''
        
        self.new_cred.save_cred()
        test_cred = Credentials ('Test','user','password','user@gmail.com')
        test_cred.save_cred()
        found_cred = Credentials.find_by_username('user')
        print(Credentials.cred_list)
        self.assertEqual(found_cred.email,test_cred.email)
        
    def test_cred_exist(self):
        '''
        tests if the user exists method
        '''
        self.new_cred.save_cred()
        cred_exists = Credentials.cred_exist('Klarys')
        self.assertTrue(cred_exists) 
        
    def test_display_all_creds(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(Credentials.display_creds(),Credentials.cred_list)            
        
   
            
        
if __name__ == '__main__':
    unittest.main()     