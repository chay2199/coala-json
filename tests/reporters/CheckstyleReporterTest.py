import os
import unittest

import xmlschema

from coala_json.reporters.CheckstyleReporter import CheckstyleReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


class CheckstyleReporterTest(unittest.TestCase):

    def test_empty(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('empty.json')) as test_file:
            loader = coalaJsonLoader()
            checkstyle = CheckstyleReporter(loader, test_file)
            self.assertTrue(checkstyle_schema.is_valid(checkstyle.to_output()))

    def test_empty_affected_code(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('empty_affected_code.json')) as test_file:
            loader = coalaJsonLoader()
            checkstyle = CheckstyleReporter(loader, test_file)
            self.assertTrue(checkstyle_schema.is_valid(checkstyle.to_output()))

    def test_section_cli(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('section_cli.json')) as test_file:
            loader = coalaJsonLoader()
            checkstyle = CheckstyleReporter(loader, test_file)
            self.assertTrue(checkstyle_schema.is_valid(checkstyle.to_output()))

    def test_section_lang(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('section_lang.json')) as test_file:
            loader = coalaJsonLoader()
            checkstyle = CheckstyleReporter(loader, test_file)
            self.assertTrue(checkstyle_schema.is_valid(checkstyle.to_output()))

    def test_null_column(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('null_column.json')) as test_file:
            loader = coalaJsonLoader()
            checkstyle = CheckstyleReporter(loader, test_file)
            self.assertTrue(checkstyle_schema.is_valid(checkstyle.to_output()))


if __name__ == '__main__':
    unittest.main()
