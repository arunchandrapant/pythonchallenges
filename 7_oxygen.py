# challenge is http://www.pythonchallenge.com/pc/def/oxygen.html

import requests
from PIL import Image
import io
import re

# download image
image = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")

# open image
img = Image.open(io.BytesIO(image.content), 'r')

# get all pixels data from image
img_list = list(img.getdata())

# get the middle row indexes
start_pixel_index = int(img.height/2) * img.width
end_pixel_index = start_pixel_index + img.width

# get middle row pixels (which are greyscale mostly)
grey_list = img_list[start_pixel_index:end_pixel_index]

color = []  # initialize empty list to store color values

# taking every 7th pixel from the starting will do the job
num = 0
while num <= len(grey_list):
    # choose only greyscale pixels
    if grey_list[num][0] == grey_list[num][1] == grey_list[num][2]:
        color.append(grey_list[num][0])
        num += 7
    else:
        num += 7

# store string values of pixel
pass_string = ""

for word in color:
    pass_string += chr(word)

# get array from pass_string
pass_array = re.findall("[0-9]+", pass_string)

# print the keyword that opens next puzzle
print("".join(map(chr, map(int, pass_array))))

# next challenge: http://www.pythonchallenge.com/pc/def/integrity.html
