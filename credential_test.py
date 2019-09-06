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
        
    def test_save_cred(self):
        '''
        this is a test to check if the account is saved
        '''
        
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)
        
   
            
        
if __name__ == '__main__':
    unittest.main()        