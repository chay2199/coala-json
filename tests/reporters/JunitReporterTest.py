import os
import unittest

import xmlschema

from coala_json.reporters.JunitReporter import JunitReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


class JunitReporterTest(unittest.TestCase):

    def test_empty(self):
        junit_schema = xmlschema.XMLSchema(get_path('junit.xsd'))
        with open(get_path('empty.json')) as file:
            loader = coalaJsonLoader()
            junit = JunitReporter(loader, file)
            self.assertTrue(junit_schema.is_valid(junit.to_output()))

    def test_empty_affected_code(self):
        junit_schema = xmlschema.XMLSchema(get_path('junit.xsd'))
        with open(get_path('empty_affected_code.json')) as file:
            loader = coalaJsonLoader()
            junit = JunitReporter(loader, file)
            self.assertTrue(junit_schema.is_valid(junit.to_output()))

    def test_section_cli(self):
        junit_schema = xmlschema.XMLSchema(get_path('junit.xsd'))
        with open(get_path('section_cli.json')) as file:
            loader = coalaJsonLoader()
            junit = JunitReporter(loader, file)
            self.assertTrue(junit_schema.is_valid(junit.to_output()))

    def test_section_lang(self):
        junit_schema = xmlschema.XMLSchema(get_path('junit.xsd'))
        with open(get_path('section_lang.json')) as file:
            loader = coalaJsonLoader()
            junit = JunitReporter(loader, file)
            self.assertTrue(junit_schema.is_valid(junit.to_output()))

    def test_null_column(self):
        junit_schema = xmlschema.XMLSchema(get_path('junit.xsd'))
        with open(get_path('null_column.json')) as file:
            loader = coalaJsonLoader()
            junit = JunitReporter(loader, file)
            self.assertTrue(junit_schema.is_valid(junit.to_output()))


if __name__ == '__main__':
    unittest.main()
