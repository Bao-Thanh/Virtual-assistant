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
wikipedia.set_lang('vi')
language = 'vi'

from sound_audio import sound_audio as sa

'''Tính năng Gửi email'''
def send_email(text):
    sa.speak('Bạn gửi email cho ai nhỉ')
    recipient = sa.get_text()
    if len(recipient) > 0:
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('luongngochungcntt@gmail.com', 'hung23081997')
        mail.sendmail(recipient, content.encode('utf-8'))
        mail.close()
        sa.speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        sa.speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')