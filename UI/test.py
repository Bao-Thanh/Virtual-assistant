import webbrowser
import re

def open_website(text):
    reg_ex = re.search('mở website (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain + '.com'
        webbrowser.open(url)

open_website('mở website wikipedia')