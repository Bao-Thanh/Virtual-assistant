import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from selenium.webdriver.chrome.options import Options

wikipedia.set_lang('vi')
language = 'vi'

path = ChromeDriverManager().install()

from sound_audio import sound_audio as sa

'''Tính năng Tìm kiếm thông tin trên google'''
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    sa.speak('Okay!')
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.google.com")
    que = driver.find_element("xpath", "//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    
'''Tính năng Mở website'''
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        sa.speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False