## given string email id or not
import re

def email(string):
    patt=r'^[\w\.-]+@[\w\.-]+\.\w+'
    if re.match(patt,string):
        print("Valid email address")
    else:
        print("Invalid ")
    
email("anuraj@gmail.com")