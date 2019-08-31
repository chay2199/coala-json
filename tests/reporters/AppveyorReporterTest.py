import unittest

from coala_json.reporters.AppveyorReporter import AppveyorReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


class AppveyorReporterTest(unittest.TestCase):

    def test_empty(self):
        loader = coalaJsonLoader()
        appveyor = AppveyorReporter(loader, 'report.xml')
        self.assertEqual(appveyor.to_output(),
                         'Permission denied or no such file or directory')
