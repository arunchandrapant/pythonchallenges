# challenge is here: http://www.pythonchallenge.com/pc/def/map.html

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

new_string = ""

# shift each char in string by +2. If hit z=123 go back to a=97
for i in string:
    if ord(i) >= 97 and ord(i) <= 122:
        new_string += chr(((ord(i) + 2 - 97) % (123-97)) + 97)
    else:
        new_string += i

print(new_string)


# printing new_string give follows:
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


# now translating the url     http://www.pythonchallenge.com/pc/def/map.html
# new url is          http://www.pythonchallenge.com/pc/def/ocr.html
