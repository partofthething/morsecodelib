# -*- coding: utf-8 -*-
'''
Unit tests
'''
import unittest

from morsecodelib import text

class TestText(unittest.TestCase):
    """
    Test text <--> code conversion
    """

    def setUp(self):
        self.message_text = 'testing text to code converSION!'
        self.message_code = ('- . ... - .. -. --.  - . -..- -  - ---  '
                             '-.-. --- -.. .  -.-. --- -. ...- . .-. ... .. --- -. -.-.--')

    def test_text_to_code(self):
        result = text.text_to_code(self.message_text)
        self.assertEqual(result, self.message_code)

    def test_code_to_text(self):
        result = text.code_to_text(self.message_code)
        self.assertEqual(result, self.message_text.upper())

    def test_sanity(self):
        """
        make sure it's compatible with itself
        """
        code1 = text.text_to_code(self.message_text)
        text1 = text.code_to_text(code1)
        code2 = text.text_to_code(text1)
        self.assertEqual(text1, self.message_text.upper())
        self.assertEqual(code1, code2)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
