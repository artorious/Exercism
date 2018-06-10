""" Test hello-world.py """
import unittest

import hello_world


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloWorldTests(unittest.TestCase):
    """ Test Cases for hello_world.hello() """
    def test_hello(self):
        """ Tests function returns when called without a parameter."""
        self.assertEqual(hello_world.hello(), 'Hello, World!')

    def test_str_input(self):
        """ Tests function returns when called with string as parameter."""
        self.assertEqual(hello_world.hello('Arthur'), 'Hello, Arthur!')

    def test_it_only_accepts_strings(self):
        """ Test func raises Exception when called with non-string arg. """
        with self.assertRaises(TypeError):
            hello_world.hello(1)


if __name__ == '__main__':
    unittest.main()
