import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x)
print(x.span())
print(x.string)
print(x.group())

x = re.findall('ai', txt)
print(x)

x = re.split('\s', txt)
print(x)

x = re.split('\s', txt, 1)
print(x)

x = re.split('\s', txt, 2)
print(x)

x = re.sub('\s','-', txt)
print(x)

x = re.sub('\s','-', txt,2)
print(x)