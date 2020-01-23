import urllib.request
import string


url = "https://www.google.com"
opener = urllib.request.FancyURLopener({})
f = opener.open(url)
content = f.read()

if "google" in content:
    print("google in: " "content")


print(content)


def random_url_length(length):
    if length > 63:
        out = length-63
    else:
        out = 0

    return out


def random_url(integer):
    uchar = "abcdefghijklmnopqrstuvwxyz"
    lchar = uchar.upper()
    numbers = "0123456789"

    length = random_url_length(integer)
    out = ""
    for i in length:
        if integer <= 25:
            out += uchar[integer]
        elif integer <= 51:
            out += lchar[(integer - 25)]
        elif integer <= 61:
            out += numbers[(integer - 51)]
        elif integer <= 62:
            out += "_"
        else:
            print("error intiger is to big")

    return out
