# Launch a Web Browser from your python code
import webbrowser

url = "https://www.amazon.com"

# Open the default web browser
webbrowser.open(url)

# Specify a specific browser
chrome = webbrowser.get('chrome')
chrome.open(url)

# Open a new window
chrome.open_new(url)

#Open a new tab
chrome.open_new_tab(url)

# documentation
# https://docs.python.org/3/library/webbrowser.html
