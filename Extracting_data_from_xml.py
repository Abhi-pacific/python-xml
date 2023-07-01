import urllib.request
import xml.etree.ElementTree as ET
mysum = 0 
working_data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1738513.xml').read()
data = ET.fromstring(working_data)
data_w = data.findall('comments/comment')
for item in data_w:
    mysum += int(item.find('count').text)
print(mysum)


""" we can also use requests here
    " import requests
      url = requests.get('http://py4e-data.dr-chuck.net/comments_1738513.xml')
      print(str(url.text))
    "
    this code will print all the data from the web page
"""