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
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        
    def test_save_user(self):
        '''
        this is a test to check if the account is saved
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
        
        
    def test_multi_user(self):
        '''
        the method is to test if we can save multiple user objects to our username list
        '''
        self.new_user.save_user()
        test_user = User('Klarys','python3','clarisseum@gmai.com')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)   
        
    def test_delete_user(self):
        '''
        the method tests if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User ('Test','user','user@gmail.com')
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1) 
        
    def test_find_by_email(self):
        '''
        test to check if we can find a user by email and display information
        '''
        self.new_user.save_user()
        test_user = User ('Test','user','user@gmail.com')
        test_user.save_user()
        found_user = User.find_by_email('user@gmail.com') 
        
        self.assertEqual(found_user.email,test_user.email)       
        
    def test_user_exist(self):
        '''
        tests if the user exists method
        '''
        self.new_user.save_user()
        user_exists = User.user_exist('Klarys')
        self.assertTrue(user_exists)    
        
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)       
        
if __name__ == '__main__':
    unittest.main()        