import os
import unittest

from coala_json.reporters.HtmlReporter import HtmlReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


class HtmlReporterTest(unittest.TestCase):

    def test_empty(self):
        with open(get_path('empty.json')) as test_file:
            loader = coalaJsonLoader()
            html_table = HtmlReporter(loader, test_file)
            with open(get_path('table_test_files/empty.html'),
                      'r') as html_file:
                html_report = html_file.read()
            self.assertEqual(html_report, html_table.to_output())

    def test_empty_affected_code(self):
        with open(get_path('empty_affected_code.json')) as test_file:
            loader = coalaJsonLoader()
            html_table = HtmlReporter(loader, test_file)
            with open(get_path('table_test_files/empty_affected_code.html'),
                      'r') as html_file:
                html_report = html_file.read()
            self.assertEqual(html_report, html_table.to_output())

    def test_section_cli(self):
        with open(get_path('section_cli.json')) as test_file:
            loader = coalaJsonLoader()
            html_table = HtmlReporter(loader, test_file)
            with open(get_path('table_test_files/section_cli.html'),
                      'r') as html_file:
                html_report = html_file.read()
            self.assertEqual(html_report, html_table.to_output())

    def test_section_lang(self):
        with open(get_path('section_lang.json')) as test_file:
            loader = coalaJsonLoader()
            html_table = HtmlReporter(loader, test_file)
            with open(get_path('table_test_files/section_lang.html'),
                      'r') as html_file:
                html_report = html_file.read()
            self.assertEqual(html_report, html_table.to_output())

    def test_null_column(self):
        with open(get_path('null_column.json')) as test_file:
            loader = coalaJsonLoader()
            html_table = HtmlReporter(loader, test_file)
            with open(get_path('table_test_files/null_column.html'),
                      'r') as html_file:
                html_report = html_file.read()
            self.assertEqual(html_report, html_table.to_output())


if __name__ == '__main__':
    unittest.main()
