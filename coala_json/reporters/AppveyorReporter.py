import requests

from coala_json.reporters.ResultReporter import ResultReporter


class AppveyorReporter(ResultReporter):
    """
    Contain methods to report test results to appveyor
    """
    def to_output(self):
        appveyor_id = self.coala_json
        with open('C:/projects/coala-json/report.xml', 'rb') as f:
            r = requests.post('https://ci.appveyor.com/api/testresults/'
                              'junit/{}'.format(appveyor_id),
                              files={'report.xml': f})
        return r.url