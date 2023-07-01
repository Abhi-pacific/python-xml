import xml.etree.ElementTree as ET
data = '''
<person>
<name>Abhishek</name>
<phone type="intl">+91 7814856070</phone>
<email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attribute',tree.find('email').get('hide'))