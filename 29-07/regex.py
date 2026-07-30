import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
x = re.split("\s", txt)
print(x)