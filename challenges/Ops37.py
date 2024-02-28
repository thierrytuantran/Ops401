#!/usr/bin/env python3

import requests
import webbrowser
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"-----"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)
# Generate a .html file to capture the contents of the HTTP response
filename = "cookie_test_response.html"
with open(filename, "w") as file:
    file.write(response_with_cookie.text)

# Open it with Firefox (or default web browser if Firefox is unavailable)
try:
    # Try to use the Firefox browser, if installed.
    browser_path = "/usr/bin/firefox" # This path may vary depending on the operating system and installation
    webbrowser.get(browser_path).open(filename)
except webbrowser.Error:
    # If Firefox is not installed, use the default browser.
    webbrowser.open(filename)
