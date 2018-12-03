import unittest
from app import app

class TestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_world_response(self):
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_task_get_all(self):
        response = self.app.get('/tasks', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_task_get_task(self):
        response = self.app.get('/tasks/task1', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_task_new_task(self):
        response = self.app.post('/tasks')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass