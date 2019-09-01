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

    def test_file(self):
        os.system('coala --json > empty.json')
        os.system('coala-json --junit -f {} -o test.xml'.format('empty.json'))
        loader = coalaJsonLoader()
        appveyor = AppveyorReporter(loader, 'test.xml')
        self.assertEqual(appveyor.to_output(), 400)
