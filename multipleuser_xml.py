import xml.etree.ElementTree as ET
data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Abhishek</name>
        </user>
        <user x = "3">
            <id>002</id>
            <name>Aditya</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(data)
my_list = stuff.findall('users/user')
for item in my_list:
    print('Name :',item.find('name').text)
    print('Id :',item.find('id').text)
    print('Attribute', item.get('x'))