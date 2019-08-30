import sys
import requests


with open('C:/projects/coala-json/report.xml', 'rb') as f:
    r = requests.post('https://ci.appveyor.com/api/testresults/'
                      'junit/{}'.format(sys.argv[1:][0]),
                      files={'report.xml': f})
print(r.url)
