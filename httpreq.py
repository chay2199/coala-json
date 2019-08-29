import requests

with open('C:/projects/coala-json/report.xml', 'r') as f:
    r = requests.post('https://ci.appveyor.com/api/testresults/'
                      'junit/$($env:APPVEYOR_JOB_ID)',
                      files={'report.xls': f})
print(r.text)
