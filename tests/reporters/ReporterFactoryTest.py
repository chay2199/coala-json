import unittest

from coala_json.reporters.cli import cli
from coala_json.loader.coalaJsonLoader import coalaJsonLoader
from coala_json.reporters.ReporterFactory import ReporterFactory


class ReporterFactoryTest(unittest.TestCase):

    def setUp(self):
        """
        Set up parser
        """
        self.loader = coalaJsonLoader()
        self.parser = cli.create_parser()

    def test_get_report(self):
        args = self.parser.parse_args(['--checkstyle'])
        factory = ReporterFactory(self.loader, self.parser, '', args)
        check = '<coala_json.reporters.CheckstyleReporter.CheckstyleReporter'
        self.assertEqual(check, str(factory.get_reporter()).split(" ")[0])

        args = self.parser.parse_args(['--junit'])
        factory = ReporterFactory(self.loader, self.parser, '', args)
        check = '<coala_json.reporters.JunitReporter.JunitReporter'
        self.assertEqual(check, str(factory.get_reporter()).split(" ")[0])

        args = self.parser.parse_args(['--tap'])
        factory = ReporterFactory(self.loader, self.parser, '', args)
        check = '<coala_json.reporters.TapReporter.TapReporter'
        self.assertEqual(check, str(factory.get_reporter()).split(" ")[0])


if __name__ == '__main__':
    unittest.main()
