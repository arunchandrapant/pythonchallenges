# url for the puzzle is: http://www.pythonchallenge.com/pc/def/linkedlist.html

import requests
import re

num = '12345'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


# function for traversing linked url
def traverse_url(url, num):
    while True:
        page = requests.get(url+num)
        if page.status_code == 200:
            content = re.findall('[0-9]+', page.text)
            if len(content) != 0:
                num = content[0]
                print(num)
            else:
                break
        else:
            break

    return num


num = traverse_url(url, num)

# the number saved in 'num' variable is the last one in the list
# check url with this number as 'nothing' parameter
# check: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044

num = str(int(num)/2)  # dividing num by 2 and proceeding again

num = traverse_url(url, num)

# trying: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82683

# go to 'nothing' value 82682 and then to 63579. Then traverse again

num = '63579'

num = traverse_url(url, num)

# go to nothing value 66831
# you will find peak.html
