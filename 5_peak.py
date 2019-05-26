# challenge: http://www.pythonchallenge.com/pc/def/peak.html

import requests
import pickle
import io

# peah hell means pickle. Download the pickle file whose link is in source.
text = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")

# load pickle data into a list
list = pickle.load(io.BytesIO(text.content))

# List looks like a character art. Try printing it
for item in list:
    for obj in item:
        print(obj[0]*obj[1], end="")
    print('\n')

# next challenge is at: http://www.pythonchallenge.com/pc/def/channel.html
