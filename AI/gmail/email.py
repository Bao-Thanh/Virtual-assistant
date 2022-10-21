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
    sa.speak('Bạn gửi email cho ai nhỉ?')
    recipient = sa.get_text()
    if len(recipient) > 0:
        url = 'mailto:' + recipient
        webbrowser.open(url)
    else:
        sa.speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')