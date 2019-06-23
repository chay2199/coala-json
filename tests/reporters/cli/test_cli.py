import os
import unittest
from unittest import mock

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
        self.assertEqual(parsed.input, None)
        self.assertEqual(parsed.output, 'test_report.xml')

    def test_with_junit_arg(self):
        """
        User passes only junit argument
        """
        parsed = self.parser.parse_args(['--junit'])
        self.assertEqual(parsed.junit, True)
        self.assertEqual(parsed.input, None)
        self.assertEqual(parsed.output, 'test_report.xml')

    def test_with_empty_junit(self):
        """
        User passes empty junit argument
        """
        parsed = self.parser.parse_args(['-f', 'test.json', '-o', 'repo.xml'])
        self.assertEqual(parsed.junit, None)
        self.assertEqual(parsed.input, 'test.json')
        self.assertEqual(parsed.output, 'repo.xml')

    def test_with_complete_args(self):
        """
        User passes complete arguments
        """
        parsed = self.parser.parse_args(['--junit', '-f', 'test.json', '-o',
                                         'repo.xml'])
        self.assertEqual(parsed.junit, True)
        self.assertEqual(parsed.input, 'test.json')
        self.assertEqual(parsed.output, 'repo.xml')

    def test_main(self):
        """
        Test for main. Note that an empty list is passed to specify explicit
        args while running pytest
        """
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.main([])
            self.assertEqual(cm.exception.code, 2)

    def test_produce_report(self):
        os.system('coala --json > {}'.format(cli.get_path('output.json')))
        parsed = self.parser.parse_args(['--junit', '-f', 'output.json',
                                         '-o', 'repo.xml'])
        self.assertIsNone(cli.produce_report(self.parser, parsed))

        parsed = self.parser.parse_args(['-f', 'output.json', '-o',
                                         'repo.xml'])
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.produce_report(self.parser, parsed)
            self.assertEqual(cm.exception.code, 2)

        parsed = self.parser.parse_args(['--junit', '-o', 'repo.xml'])
        with self.assertRaisesRegex(SystemExit, '2') as cm:
            cli.produce_report(self.parser, parsed)
            self.assertEqual(cm.exception.code, 2)

    @staticmethod
    def test_main_call():
        with mock.patch.object(cli, "main", return_value=42):
            with mock.patch.object(cli, "__name__", "__main__"):
                with mock.patch.object(cli.sys, 'exit') as mock_exit:
                    cli.main_call()
                    assert mock_exit.call_args[0][0] == 42


if __name__ == "__main__":
    unittest.main()
