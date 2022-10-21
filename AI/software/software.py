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

'''Tính năng Mở ứng dụng'''
def open_application(text):
    if "phần mềm" in text:
        subtext = text[12: len(text)]
        sa.speak("Mở phần mềm " + subtext)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\" + subtext)
    elif "word" in text:
        sa.speak("Mở Microsoft Word")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        sa.speak("Mở Microsoft Excel")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    else:
        sa.speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")