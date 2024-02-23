from django.test import TestCase


# run test --> python manage.py test
# only store --> python manage.py test store.tests
# python manage.py test store.tests.tests ExampleTestClass
class ExampleTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Run once to create non-modified data to be used by all class methods"
              "use this to create objects or data that is not to be modified by any of the test methods")
        pass

    def setUp(self):
        print("Run once for every test-method. Used when you want to have a clean set of data for each test method")

    def tearDown(self):
        print("Run after all the tests are completed to clean up any data")

    def test_false_is_false(self):
        print("false is supposed to be false")
        self.assertFalse(False)

    def test_view_return_redirect(self):
        self.assertTrue(True)
