import requests

url = ('https://ci.appveyor.com/api/testresults/'
       'junit/$($env:APPVEYOR_JOB_ID)')
files = {'file': open('$APPVEYOR_BUILD_FOLDER/report.xml', 'r')}
r = requests.post(url, files=files)
print(r.text)
