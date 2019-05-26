# the challenge is here: http://www.pythonchallenge.com/pc/def/ocr.html

import requests
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

# get html page
page = requests.request("GET", url).text

# get comment from html page
comment = re.search("<!--(.|\n|\r)*?-->", page)
# above re is not working with findall
# for using with search it can be simplified much. But intention was to find with findall

page = page[comment.span()[1]:]

page = re.sub("\r|\n", "", page)
page = re.sub("<!--|-->", "", page)

# now create a table containing repeated occurences of a char in 'page' string

dict = {}

for s in page:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1

dict

# from the above dict, you will know that 'equality' are the characters that...
# ...have occured only 2 times
