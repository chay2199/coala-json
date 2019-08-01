import os
import sys
import unittest
from io import StringIO

from coala_json.reporters.cli import cli


class CliTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up parser
        """
        self.parser = cli.create_parser()

    def test_with_empty_args(self):
        """
        User passes no args
        """
        parsed = self.parser.parse_args([])
        self.assertEqual(parsed.junit, None)
        self.assertEqual(parsed.checkstyle, None)
        self.assertEqual(parsed.input, None)
        self.assertEqual(parsed.output, None)

    def test_with_junit_arg(self):
        """
        User passes only junit argument
        """
        parsed = self.parser.parse_args(['--junit'])
        self.assertEqual(parsed.junit, True)
        self.assertEqual(parsed.checkstyle, None)
        self.assertEqual(parsed.input, None)
        self.assertEqual(parsed.output, None)

    def test_with_checkstyle_arg(self):
        """
        User passes only junit argument
        """
        parsed = self.parser.parse_args(['--checkstyle'])
        self.assertEqual(parsed.junit, None)
        self.assertEqual(parsed.checkstyle, True)
        self.assertEqual(parsed.input, None)
        self.assertEqual(parsed.output, None)

    def test_with_empty_junit(self):
        """
        User passes empty junit argument
        """
        parsed = self.parser.parse_args(['--checkstyle', '-f', 'test.json',
                                         '-o', 'report.xml'])
        self.assertEqual(parsed.junit, None)
        self.assertEqual(parsed.checkstyle, True)
        self.assertEqual(parsed.input, 'test.json')
        self.assertEqual(parsed.output, 'report.xml')

    def test_with_complete_args(self):
        """
        User passes complete arguments
        """
        parsed = self.parser.parse_args(['--junit', '-f',
                                         'test.json', '-o', 'junit.xml'])
        self.assertEqual(parsed.junit, True)
        self.assertEqual(parsed.checkstyle, None)
        self.assertEqual(parsed.input, 'test.json')
        self.assertEqual(parsed.output, 'junit.xml')

    def test_main(self):
        sys.argv = ['']
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.main()
            self.assertEqual(cm.exception.code, 2)

    def test_stdout_output(self):
        os.system('coala --json > {}'.format(cli.get_path('output.json')))
        parsed = self.parser.parse_args(['--tap', '-f', 'output.json'])
        standard_out, standard_err = StringIO(), StringIO()
        sys.stdout, sys.stderr = standard_out, standard_err
        cli.produce_report(self.parser, parsed)
        std_out, std_err = standard_out.getvalue(), standard_err.getvalue()
        self.assertEqual('TAP version 13\n1..1\nok 1 - coala\n...', std_out)
        self.assertEqual('', std_err)

    def test_produce_report(self):
        parsed = self.parser.parse_args(['--junit', '-o', 'report.xml'])
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.produce_report(self.parser, parsed)
            self.assertEqual(cm.exception.code, 2)

        os.system('coala --json > {}'.format(cli.get_path('output.json')))
        parsed = self.parser.parse_args(['--junit', '-f', 'output.json',
                                         '-o', 'report.xml'])
        self.assertIsNone(cli.produce_report(self.parser, parsed))

        parsed = self.parser.parse_args(['--checkstyle', '-f', 'output.json',
                                         '-o', 'report.xml'])
        self.assertIsNone(cli.produce_report(self.parser, parsed))

        parsed = self.parser.parse_args(['--tap', '-f', 'output.json'])
        self.assertIsNone(cli.produce_report(self.parser, parsed))

        parsed = self.parser.parse_args(['-f', 'output.json', '-o',
                                         'report.xml'])
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.produce_report(self.parser, parsed)
            self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
