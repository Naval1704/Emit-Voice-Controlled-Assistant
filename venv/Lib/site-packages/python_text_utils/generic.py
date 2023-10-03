import sys
import re, string

# Check if python version is 2
PY2 = sys.version_info.major == 2

# Regex for splitting a string by any punctuation
regex = re.compile(r'[%s\s]+' % re.escape(string.punctuation))

class Generic(object):
    """
    Class containing generic text utils.
    """

    @classmethod
    def strip_punctuation_unicode(cls, text):
        """
        Removes punctuation from string.

        :param text:        unicode or str string.
        :return:            unicode string without punctuation
        """
        text = cls.to_unicode(text)
        return " ".join(regex.split(text)).strip()

    @staticmethod
    def to_unicode(text):
        """
        Converts string to unicode if str.

        :param text:        str to convert to unicode
        :return:            unicode repr of string
        """
        if isinstance(text, str) and PY2:
            text = text.decode('utf-8')
        return text