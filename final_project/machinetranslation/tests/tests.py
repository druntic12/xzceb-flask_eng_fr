from translator import english_fo_french, french_to_english
import unittest

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(''), '')
        #self.assertEqual(frenchToEnglish('Bonjour'),'Helleeo')

class TestenglishToFrench(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(english_fo_french('Hello'),'Bonjour')
        self.assertEqual(english_fo_french(''), '')
        self.assertEqual(english_fo_french(' '), ' ')
        #self.assertEqual(englishToFrench('H'),'Bonjour')
        

        
        

unittest.main()