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

    def test_severity_info(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('checkstyle_test_files/severity_info.xml')) as test:
            self.assertTrue(checkstyle_schema.is_valid(test))

        with open(get_path('severity_info.json')) as test_file:
            loader = coalaJsonLoader()
            check = CheckstyleReporter(loader, test_file)
            with open(get_path('checkstyle_test_files/severity_info.xml'),
                      'r') as check_file:
                check_report = check_file.read()
            self.assertEqual(check_report, check.to_output())

    def test_severity_warning(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('checkstyle_test_files/severity_warning.xml')) as \
                test:
            self.assertTrue(checkstyle_schema.is_valid(test))

        with open(get_path('severity_warning.json')) as test_file:
            loader = coalaJsonLoader()
            check = CheckstyleReporter(loader, test_file)
            with open(get_path('checkstyle_test_files/severity_warning.xml'),
                      'r') as check_file:
                check_report = check_file.read()
            self.assertEqual(check_report, check.to_output())

    def test_severity_error(self):
        checkstyle_schema = xmlschema.XMLSchema(get_path('checkstyle.xsd'))
        with open(get_path('checkstyle_test_files/severity_error.xml')) as \
                test:
            self.assertTrue(checkstyle_schema.is_valid(test))

        with open(get_path('severity_error.json')) as test_file:
            loader = coalaJsonLoader()
            check = CheckstyleReporter(loader, test_file)
            with open(get_path('checkstyle_test_files/severity_error.xml'),
                      'r') as check_file:
                check_report = check_file.read()
            self.assertEqual(check_report, check.to_output())


if __name__ == '__main__':
    unittest.main()
