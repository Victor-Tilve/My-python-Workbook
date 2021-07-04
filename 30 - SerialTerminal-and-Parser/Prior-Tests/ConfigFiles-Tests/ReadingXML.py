from xml.dom import minidom


''' 
En este archivo puedo instanciar el objeto "Serial", de tal forma que la funcion retorne el objeto
'''
# parse an xml file by name
mydoc = minidom.parse('config.xml')

items = mydoc.getElementsByTagName('item')
pruebas = mydoc.getElementsByTagName('prueb')

""" # all item attributes
print('\nAll attributes:')
for elem in items:
    print(elem.firstChild.data)
 """


#Type
print("Items' Type:" + str(type(items)))

# one specific item attribute
print('Item #1 attribute:')
print(items[0].attributes['name'].value)

# all item attributes
print('\nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)