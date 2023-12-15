## Valid URL
# import re

# def is_valid_url(url):
#   pattern = re.compile(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)')
#   return pattern.match(url)

# str=input("Enter URL : ")
# print(is_valid_url(str))

import re

def is_valid_url(url):
    pattern = re.compile(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#?&//=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%._\+~#?&//=]*)', re.IGNORECASE)
    return pattern.match(url)

url_input = input("Enter URL: ")
print(is_valid_url(url_input))
# is_valid_url(url_input)