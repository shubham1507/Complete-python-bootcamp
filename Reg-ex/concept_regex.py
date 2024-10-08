import re

text = "abb123foo"
mo = re.search('\d\d\d', text)
print(mo)
