import os
import unittest
import requests_mock
from unittest.mock import patch

from coala_json.reporters.AppveyorReporter import AppveyorReporter
from coala_json.loader.coalaJsonLoader import coalaJsonLoader


def get_path(filename):
    file_path = os.path.join(os.path.dirname(__file__),
                             'test_files/',
                             filename)
    return file_path


@requests_mock.mock()
class AppveyorReporterTest(unittest.TestCase):

    def test_file_not_found(self):
        loader = coalaJsonLoader()
        appveyor = AppveyorReporter(loader, 'report.xml')
        self.assertEqual(appveyor.to_output(),
                         'Permission denied or no such file or directory')

    def test_file(self, m):
        with patch.dict('os.environ', {'APPVEYOR_JOB_ID': '12345',
                                       'APPVEYOR_BUILD_FOLDER': './'}):
            loader = coalaJsonLoader()
            appveyor = AppveyorReporter(loader, 'AppveyorReporterTest.py')
            m.post('https://ci.appveyor.com/api/testresults/junit/{}'
                   .format(os.getenv('APPVEYOR_JOB_ID')), status_code=200)
            self.assertEqual(appveyor.to_output(),
                             'https://ci.appveyor.com/api/testresults/junit/12345')


if __name__ == '__main__':
    unittest.main()
