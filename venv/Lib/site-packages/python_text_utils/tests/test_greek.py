# -*- coding: utf-8 -*-

import unittest

from python_text_utils.greek import Greek

class TestGreek(unittest.TestCase):

    def test_strip_accent_from_greek_string_with_accent(self):
        with_accent = u'λόγος'
        without_accent = u'λογος'
        self.assertEqual(Greek.strip_accent_unicode(with_accent),
                         without_accent)

    def test_strip_accent_from_greek_string_without_accent(self):
        without_accent = u'πιτα'
        self.assertEqual(Greek.strip_accent_unicode(without_accent),
                         without_accent)

    def test_strip_accent_from_latin_string(self):
        latin_string = u'whatever'
        self.assertEqual(Greek.strip_accent_unicode(latin_string),
                         latin_string)

    def test_strip_accent_non_unicode(self):
        with_accent = 'λόγος'
        without_accent = u'λογος'
        self.assertEqual(Greek.strip_accent_unicode(with_accent),
                         without_accent)

    def test_strip_accent_uppercase(self):
        uppercase_with_accent = 'ΛΌΓΟΣ'
        uppercase_without_accent = u'ΛΟΓΟΣ'
        self.assertEqual(Greek.strip_accent_unicode(uppercase_with_accent),
                         uppercase_without_accent)

    def test_strip_accent_and_punctuation_from_string_with_accent_and_punctuation(self):
        uppercase_with_accent = 'λόγος-απειλή'
        uppercase_without_accent = u'λογος απειλη'
        self.assertEqual(Greek.strip_punctuation_and_accent_unicode(uppercase_with_accent),
                         uppercase_without_accent)

    def test_strip_accent_and_punctuation_from_string_without_accent_and_punctuation(self):
        uppercase_with_accent = 'λόγος απειλή'
        uppercase_without_accent = u'λογος απειλη'
        self.assertEqual(Greek.strip_punctuation_and_accent_unicode(uppercase_with_accent),
                         uppercase_without_accent)

    def test_strip_accent_and_punctuation_from_latin_string(self):
        uppercase_with_accent = 'logos apeilh'
        uppercase_without_accent = u'logos apeilh'
        self.assertEqual(Greek.strip_punctuation_and_accent_unicode(uppercase_with_accent),
                         uppercase_without_accent)

    def test_strip_accent_and_punctuation_from_uppercase_string(self):
        uppercase_with_accent = 'ΛΌΓΟΣ-ΑΠΕΙΛΉ.ΚΙ/ΕΣΎ+ΜΑΖΙ.ΓΙΌ.'
        uppercase_without_accent = u'ΛΟΓΟΣ ΑΠΕΙΛΗ ΚΙ ΕΣΥ ΜΑΖΙ ΓΙΟ'
        self.assertEqual(Greek.strip_punctuation_and_accent_unicode(uppercase_with_accent),
                         uppercase_without_accent)

