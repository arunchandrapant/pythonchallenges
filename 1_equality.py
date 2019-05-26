# http://www.pythonchallenge.com/pc/def/equality.html

import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"

# get the challenge source
page = requests.get(url).text

# comment in the html page has the challenge. get it
page = re.findall(r'<!--[\s|\S]+-->', page)

page = page[0]

page = re.sub("<!--", "", page)
page = re.sub("\n|\r", "", page)
page = re.sub("-->", "", page)


# find one small letter surrounded by exactly 3 big bodyguards on each side
page = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', page)
page


# printing out such cases will give you following:
# ['qIQNlQSLi',
# 'eOEKiVEYj',
# 'aZADnMCZq',
# 'bZUTkLYNg',
# 'uCNDeHSBj',
# 'kOIXdKBFh',
# 'dXJVlGZVm',
# 'gZAGiLQZx',
# 'vCJAsACFl',
# 'qKWGtIDCj']


# therefore next link has 'linkedlist' in it
# http://www.pythonchallenge.com/pc/def/linkedlist.html
