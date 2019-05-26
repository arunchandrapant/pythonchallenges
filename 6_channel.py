# challenge is here: http://www.pythonchallenge.com/pc/def/channel.html

import re
import zipfile
import requests
import io

# after a lot of time waste and head banging, download a zip file
zip_file = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')

# load zip file as zipfile object
archive = zipfile.ZipFile(io.BytesIO(zip_file.content), 'r')

# get list of all file in archive
file_list = archive.namelist()

start_file = '90052.txt'
keyword = ''

# after a lot of futile traversing, focus on collecting comments from each file
while True:
    text = archive.open(start_file).read().decode()  # open file to get comtnet
    num = re.findall('[0-9]+', text)
    keyword += archive.getinfo(start_file).comment.decode()  # get comments
    if len(num) > 0:
        start_file = num[0] + '.txt'
    else:
        break

# print the pattern
print("".join([i for i in keyword]))

# after going to the url hockey.html, you get to oxygen.html
# next challenge is: http://www.pythonchallenge.com/pc/def/oxygen.html
