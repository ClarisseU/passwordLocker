import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Class that tests the case for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Klarys','python3','clarisseum@gmai.com')
        
    def test_init(self):
        '''
        first_test is to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Klarys')
        self.assertEqual(self.new_user.password,'python3')
        self.assertEqual(self.new_user.email,'clarisseum@gmai.com')
        
    def test_save_user(self):
        '''
        this is a test to check if the account is saved
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
            
        
if __name__ == '__main__':
    unittest.main()        