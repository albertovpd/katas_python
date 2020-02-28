# Scraping: Get the Year a CodeWarrior Joined

import urllib.request as L
from bs4 import BeautifulSoup
import re

def get_member_since(username):
    request = L.urlopen('https://www.codewars.com/users/'+username)
    member = BeautifulSoup(request, "html.parser").find_all("div",class_="stat")
    return [x.text[13:] for x in member if re.search("Member Since",x.text)][0]