import unittest

import hello_world


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        """ Tests function returns when called without a parameter."""
        self.assertEqual(hello_world.hello(), 'Hello, World!')

    
    def test_str_input(self):
        """ Tests function returns when called with string as parameter."""
        self.assertEqual(hello_world('Arthur'), 'Hello, Arthur!')

    def test_it_only_accepts_strings(self):
        """ Tests function raises TypeError if called with a non-string """
        self.assertRaises(hello_world.TypeError, hello_world.hello, 1)
if __name__ == '__main__':
    unittest.main()
