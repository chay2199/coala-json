import os
import unittest

from coala_json.reporters.AppveyorReporter import AppveyorReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


class AppveyorReporterTest(unittest.TestCase):

    def test_file_not_found(self):
        loader = coalaJsonLoader()
        appveyor = AppveyorReporter(loader, 'report.xml')
        self.assertEqual(appveyor.to_output(),
                         'Permission denied or no such file or directory')

    @unittest.skipUnless(os.getenv('APPVEYOR') == 'True', 'Skip unless AppVeyor'
                                                          ' CI test')
    def test_file(self):
        loader = coalaJsonLoader()
        appveyor = AppveyorReporter(loader, 'report.xml')
        self.assertEqual(appveyor.to_output(), 400)
