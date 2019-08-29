import requests

url = ('https://ci.appveyor.com/api/testresults/'
       'junit/$($env:APPVEYOR_JOB_ID)')
files = {'file': open('C:/projects/coala-json/report.xml', 'r')}
r = requests.post(url, files=files)
print(r.text)
