from xml.etree import ElementTree

# Just to validate that I can read the XML file.

XML = ElementTree.parse("C:\\seleniumDrivers\\config.xml")
print(XML.find("URL").text)
