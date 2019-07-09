import os
import unittest

from coala_json.reporters.TapReporter import TapReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


class TapReporterTest(unittest.TestCase):

    def test_empty(self):
        with open(get_path('empty.json')) as test_file:
            loader = coalaJsonLoader()
            tap = TapReporter(loader, test_file)
            self.assertEqual('TAP version 13\n1..1\nok 1 - coala\n...',
                             tap.to_output())

    def test_empty_affected_code(self):
        with open(get_path('empty_affected_code.json')) as test_file:
            loader = coalaJsonLoader()
            tap = TapReporter(loader, test_file)
            with open(get_path('tap_test_files/empty_affected_code.txt'),
                      'r') as tap_file:
                tap_report = tap_file.read()
            self.assertEqual(tap_report, tap.to_output())

    def test_section_cli(self):
        with open(get_path('section_cli.json')) as test_file:
            loader = coalaJsonLoader()
            tap = TapReporter(loader, test_file)
            with open(get_path('tap_test_files/section_cli.txt'),
                      'r') as tap_file:
                tap_report = tap_file.read()
            self.assertEqual(tap_report, tap.to_output())

    def test_section_lang(self):
        with open(get_path('section_lang.json')) as test_file:
            loader = coalaJsonLoader()
            tap = TapReporter(loader, test_file)
            with open(get_path('tap_test_files/section_lang.txt'),
                      'r') as tap_file:
                tap_report = tap_file.read()
            self.assertEqual(tap_report, tap.to_output())

    def test_null_column(self):
        with open(get_path('null_column.json')) as test_file:
            loader = coalaJsonLoader()
            tap = TapReporter(loader, test_file)
            with open(get_path('tap_test_files/null_column.txt'),
                      'r') as tap_file:
                tap_report = tap_file.read()
            self.assertEqual(tap_report, tap.to_output())


if __name__ == '__main__':
    unittest.main()
