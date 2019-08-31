import os
import requests

from coala_json.reporters.ResultReporter import ResultReporter


class AppveyorReporter(ResultReporter):
    """
    Contain methods to report test results to appveyor
    """

    def to_output(self):
        file_to_upload = self.coala_json
        appveyor_job_id = os.environ['APPVEYOR_JOB_ID']
        with open('C:/projects/coala-json/{}'.format(file_to_upload),
                  'rb') as f:
            r = requests.post('https://ci.appveyor.com/api/testresults/'
                              'junit/{}'.format(appveyor_job_id),
                              files={'report.xml': f})
        return r.url
